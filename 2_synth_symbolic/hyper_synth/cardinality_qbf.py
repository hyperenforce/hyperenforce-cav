import math

from hyper_synth.qbf import (AND, EQUIVALENT, EXISTS, FALSE, IMPLIES, NOT, OR,
                             TRUE)
from hyper_synth.util import flatten_to_list


def at_most_k_form(v, k, var_pool, coeffs=None):
    """
    Formula satisfied when at most `k` of the variables in `v` are true.

    Parameters
    ----------
    v : iter[int]
        The variables to bound
    k : int
        The bound
    name : str or tuple or int
        The name to use in creating auxiliary variables. Must be unique from other calls.
    bvars : pysat.IDPool
        The pool of variables (used for output and auxiliary variable creation)
    """
    if k == 0:
        return NOT(OR(*v))
    if k >= len(v):
        return TRUE
    enc = TotalizerEncodingQBF(v, var_pool, coeffs=coeffs)
    enc.encode()
    unary = enc.v_out_unary
    inner_form = -unary[k]
    form = enc.apply(inner_form)
    return form


def compare_count_form(v1, v2, var_pool, coeffs1=None, coeffs2=None):
    """
    Formula satisfied when the number of true variables in `v1` is less than that in `v2`

    Parameters
    ----------
    v1 : iter[int]
        The first set of variables
    v2 : iter[int]
        The second set of variables
    name : str or tuple or int
        The name to use in creating auxiliary variables. Must be unique from other calls.
    bvars : pysat.IDPool
        The pool of variables (used for output and auxiliary variable creation)
    """
    enc1 = TotalizerEncodingQBF(v1, var_pool, coeffs=coeffs1)
    enc2 = TotalizerEncodingQBF(v2, var_pool, coeffs=coeffs2)
    enc1.encode()
    enc2.encode()
    unary1 = enc1.v_out_unary
    unary2 = enc2.v_out_unary
    inner_form = AND(*[IMPLIES(cb1, cb2) for cb1, cb2 in zip(unary1, unary2)])
    if len(unary1) > len(unary2):
        inner_form.add_args(NOT(unary1[len(unary2)]))
    form = enc1.apply(enc2.apply(inner_form))
    return form


class _TotalizerNode:

    def __init__(self, coord, v_in):
        self.coord = tuple(coord)
        self.v_in = tuple(v_in)
        self.v_link = None

    @property
    def label(self):
        return len(self.v_in)

    @property
    def is_leaf(self):
        return self.label == 1

    @property
    def is_root(self):
        return self.coord == ()

    def get_children(self):
        if self.is_leaf:
            return ()
        return (_TotalizerNode(self.coord + (0,), self.v_in[:math.floor(self.label / 2)]),
                _TotalizerNode(self.coord + (1,), self.v_in[math.floor(self.label / 2):]))


class TotalizerEncodingQBF:
    """
    This class is creates a unary encoding of the cardinality of a set of Boolean variables (the ones set to true).
    This uses the method of
        Bailleux, O., Boufkhad, Y. (2003). Efficient CNF Encoding of Boolean Cardinality Constraints. In: Rossi, F. (eds)
        Principles and Practice of Constraint Programming

    Note that the unary encoding of integers used here is least-significant-bit first
    """

    def __init__(self, v_in, var_pool, coeffs=None):
        if len(v_in) == 0:
            raise ValueError("Number of variables must be at least one")
        if coeffs is None:
            coeffs = [1] * len(v_in)
        if not len(coeffs) == len(v_in):
            raise ValueError("Wrong number of coefficients in sum")
        if any(c < 0 for c in coeffs):
            raise NotImplementedError("Only nonnegative coefficients are supported now")
        #if set(coeffs) != {1}:
        #    raise NotImplemented("Only coefficients/costs of 1 are supported now")

        # TODO - use better encoding for coefficients
        # coefficients are naively encoded by repeating variables
        self.v_in = tuple(flatten_to_list([[v] * c for v, c in zip(v_in, coeffs)]))
        #self.v_in = tuple(v_in)
        self.trivial = len(self.v_in) == 1
        self.var_pool = var_pool
        if not self.trivial:
            self.quant_vars = set()

            self.root = _TotalizerNode((), self.v_in)
            self.v_out_unary = self.node_vars(self.root)
            self.inner_form = AND()
        else:
            self.v_out_unary = self.v_in
            self.inner_form = TRUE

    def encode(self):
        if not self.trivial:
            self._encode_subtree(self.root)
            self.inner_form = self.inner_form.to_simplified()

    def apply(self, form):
        if self.trivial:
            return AND(form, self.inner_form)
        return EXISTS(self.quant_vars, AND(form, self.inner_form))

    def _encode_subtree(self, node):
        r = node
        a, b = node.get_children()

        rv = self.aug_vars(self.node_vars(r))
        av = self.aug_vars(self.node_vars(a))
        bv = self.aug_vars(self.node_vars(b))

        m1 = a.label
        m2 = b.label
        m = r.label

        clauses = [OR(NOT(av[alpha]), NOT(bv[beta]), rv[alpha + beta]) &
                   OR(av[alpha + 1], bv[beta + 1], NOT(rv[alpha + beta + 1]))
                   for alpha in range(min(m1, m) + 1)
                   for beta in range(min(m2, m - alpha) + 1)
                   ]
        self.inner_form.add_args(*clauses)

        for c in (a, b):
            if not c.is_leaf:
                self._encode_subtree(c)

    def aug_vars(self, v):
        # TODO replace this with explicit variable indexing in `_encode_subtree`
        # sorry for this hack, it matches the definitions in the paper exactly
        return (TRUE,) + v + (FALSE,)

    def node_vars(self, node):
        if node.is_leaf:
            # leaf nodes add input bits
            return node.v_in
        if node.v_link is None:
            # if new node, create new partial sum vars (link vars)
            node.v_link = self.var_pool.get_vars(node.label)
            self.quant_vars |= set(node.v_link)
        return node.v_link
