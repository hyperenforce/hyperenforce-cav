import itertools
import re
from collections import deque

from hyper_synth.qbf import AND, EXISTS, FALSE, FORALL, NOT, OR, SYMBOL, TRUE
from hyper_synth.util import flatten_to_list
from pyeda.boolalg.expr import (AndOp, Complement, NotOp, One, OrOp, Variable,
                                Zero)
from pyeda.boolalg.minimization import espresso_tts
from pyeda.boolalg.table import truthtable, ttvar


class QCIRWriter:

    def __init__(self, f, qbf, free_vars, free_as_existential=True, add_true_var=False):
        self.f = f
        self.qbf = qbf
        self.free_vars = list(set(free_vars))
        self.free_as_existential = free_as_existential
        self.add_true_var = add_true_var

        self.output_expr = None
        self.output_var = None

        self.num_vars = self.qbf.max_var
        if add_true_var:
            self.num_vars += 1
            self.true_var = self.num_vars
            self.false_var = -self.true_var
            self.free_vars.append(self.true_var)

    def _write_line(self, s):
        self.f.write(s + "\n")

    def _write_function(self, operator, args):
        self._write_line(f"{operator}({', '.join([str(v) for v in args])})")

    def _write_assignment(self, var, operator, args):
        self._write_line(f"{var} = {operator}({', '.join([str(v) for v in args])})")

    def _write_quantifier_assignment(self, var, operator, args1, arg2):
        self._write_line(f"{var} = {operator}({', '.join([str(v) for v in args1])}; {str(arg2)})")

    def _write_format(self):
        self._write_line(f"#QCIR-G14")

    def _write_quantifier_block(self):
        if self.free_vars:
            # Write design variables in outer most quantifier
            outer_str = "exists" if self.free_as_existential else "free"
            self._write_function(outer_str, self.free_vars)

        expr = self.qbf
        while isinstance(expr, FORALL) or isinstance(expr, EXISTS):
            self._write_function(expr.quantifier, expr.quant_variables)
            expr = expr.quant_expr

        if self.add_true_var:
            self.output_expr = AND(expr, self.true_var)
        else:
            self.output_expr = expr

    def _write_output(self):
        self.output_var = self._get_gate_var(self.output_expr)
        self._write_function("output", [self.output_var])

    def _write_gates(self):
        # Write gates (and non-prenex quantifiers)
        expr_to_write = deque()
        expr_to_write.append((self.output_expr, self.output_var))
        while expr_to_write:
            expr, expr_var = expr_to_write.popleft()

            if expr.is_literal:
                inner_var = self._get_gate_var(expr)
                self._write_assignment(expr_var, "and", [inner_var])
            elif isinstance(expr, NOT):
                inner_var = self._get_gate_var(expr.inner_expr)
                self._write_assignment(expr_var, "and", [-inner_var])
                expr_to_write.append((expr.inner_expr, inner_var))
            elif isinstance(expr, FORALL) or isinstance(expr, EXISTS):
                inner_var = self._get_gate_var(expr.quant_expr)
                self._write_quantifier_assignment(expr_var, expr.quantifier, expr.quant_variables, inner_var)
                expr_to_write.append((expr.quant_expr, inner_var))
            else:
                inner_vars = [self._get_gate_var(sub_expr) for sub_expr in expr.operands]
                self._write_assignment(expr_var, expr.operator, inner_vars)
                expr_to_write.extend([p for p in (zip(expr.operands, inner_vars)) if not p[0].is_literal])

    def _get_gate_var(self, sub_expr):

        """
        Get a variable to represent the given sub-expression represented as a gate in the circuit.
        Uses existing variables for literals

        Parameters
        ----------
        sub_expr : _Expression

        Returns
        -------
        var : _VariableName
        """
        if sub_expr is TRUE:
            if not self.add_true_var:
                raise AttributeError("Must add true variable if TRUE is present in QBF")
            return self.true_var
        elif sub_expr is FALSE:
            if not self.add_true_var:
                raise AttributeError("Must add true variable if FALSE is present in QBF")
            return self.false_var
        elif sub_expr.is_literal:
            return sub_expr.var
        else:
            self.num_vars += 1
            return self.num_vars

    def write(self):
        self._write_format()
        self._write_quantifier_block()
        self._write_output()
        self._write_gates()


def _read_decorator(line_func):
    def read_func(reader):
        while line := reader.f.readline():
            if not line_func(reader, line):
                return
    return read_func


def _ignore_comment_decorator(line_func):
    def ig_line_func(reader, line):
        if line.startswith("#"):
            return True
        return line_func(reader, line)
    return ig_line_func


# Regex stuff for parsing qcir files

def _pad(t):
    return fr"\s*{t}\s*"

def _cap(t):
    # match regex `t` with padding and capture `t`
    return _pad(fr"({t})")

def _csl(t):
    # match a Comma-Separated List of `t` (can be empty)
    return fr"(?:\s*|(?:{_pad(t)}(?:,{_pad(t)})*))"

def _func(fname, arg):
    return fr"{fname}\({arg}\)\s*"

def _assign(val, fname, arg):
    return fr"{val}={_func(fname,arg)}"

def _line(l):
    return fr"^{l}$"

_var = r"(?:[1-9]\d*)" # variable
_word = r"\w+" # function/operator names
_lit = fr"-?{_var}" #  literals are variables or their negations
_cap_list_list = _cap(_csl(_lit)) # capture a list of literals
_cap_quant_list = fr"{_cap(_csl(_var))};{_cap(_lit)}" # capture a list of variables and a literal after a semicolon


class QCIRReader:

    def __init__(self, f):
        self.f = f

        self.subs_dict = {}
        self.output_var = None
        self.num_vars = 0
        self.qbf = None
        self.outer_quant_vars = []
        self.outer_quant_types = []

    def _parse_var_list(self, s):
        return [int(v) for v in s.split(",") if v and not v.isspace()]

    def _parse_function(self, line):
        m = re.search(_line(_func(_cap(_word), _cap_list_list)), line)
        if m is None:
            return None
        func_name = m.group(1)
        args = self._parse_var_list(m.group(2))
        return func_name, args

    def _parse_assignment(self, line):
        m = re.search(_line(_assign(_cap(_var), _cap(_word), _cap_list_list)), line)
        if m is None:
            return None
        val = int(m.group(1))
        func_name = m.group(2)
        args = self._parse_var_list(m.group(3))
        return val, func_name, args

    def _parse_quantifier_assignment(self, line):
        m = re.search(_line(_assign(_cap(_var), _cap(_word), _cap_quant_list)), line)
        if m is None:
            return None
        val = int(m.group(1))
        func_name = m.group(2)
        quant_vars = self._parse_var_list(m.group(3))
        arg = int(m.group(4))
        return val, func_name, quant_vars, arg

    def _parse_quant(self, quant_str):
        if quant_str in {"exists", "free"}:
            return EXISTS
        if quant_str == "forall":
            return FORALL
        return None

    def _parse_op(self, op_str):
        if op_str == "and":
            return AND
        if op_str == "or":
            return OR
        return None

    @_read_decorator
    def _read_format(self, line):
        sp = line.strip().split(" ")
        assert sp[0] == "#QCIR-G14"
        if len(sp) > 1:
            self.num_vars = int(sp[1])
            assert self.num_vars > 0
        return False

    @_read_decorator
    @_ignore_comment_decorator
    def _read_quantifier_and_output_block(self, line):
        quant_info = self._parse_function(line)
        assert quant_info is not None
        quant_name, quant_vars = quant_info
        if quant_name == "output" and len(quant_vars) == 1:
            self.output_var = quant_vars[0]
            return False
        quant_type = self._parse_quant(quant_name)
        assert quant_type is not None
        self.outer_quant_types.append(quant_type)
        self.outer_quant_vars.append(quant_vars)
        return True

    @_read_decorator
    @_ignore_comment_decorator
    def _read_gates(self, line):
        if (op_info := self._parse_assignment(line)) is not None:
            val, op_name, args = op_info
            op_type = self._parse_op(op_name)
            if op_type is None:
                raise ValueError("Invalid operator. Must be and/or")
            self.subs_dict[val] = op_type(*args)
        elif (quant_info := self._parse_quantifier_assignment(line)) is not None:
            val, quant_name, quant_vars, arg = quant_info
            quant_type = self._parse_quant(quant_name)
            if quant_type is None:
                raise ValueError("Invalid quantifier. Must be forall/exists/free")
            self.subs_dict[val] = quant_type(quant_vars, arg)
        else:
            raise ValueError("Invalid gate")
        return True

    def read(self):
        self._read_format()
        self._read_quantifier_and_output_block()
        self._read_gates()

        form = self.output_var
        for quant_type, quant_vars in reversed(list(zip(self.outer_quant_types, self.outer_quant_vars))):
            form = quant_type(quant_vars, form)

        # TODO fix this inefficient hack
        old_form = None
        while old_form != form:
            old_form = form
            form = form.substitute(self.subs_dict)
        self.qbf = form
        # self.qbf = form.substitute(self.subs_dict)

        return self.qbf


def qbf_from_pyeda(form, bvars):
    """

    Parameters
    ----------
    form : pyeda.boolalg.expr.Expression
    bvars : IDPool

    """
    if isinstance(form, AndOp):
        return AND(*[qbf_from_pyeda(inp, bvars) for inp in form.xs])
    if isinstance(form, OrOp):
        return OR(*[qbf_from_pyeda(inp, bvars) for inp in form.xs])
    if isinstance(form, NotOp):
        return NOT(qbf_from_pyeda(form.xs[0], bvars))
    if isinstance(form, Complement):
        return SYMBOL(-bvars.id((form.inputs[0].name, *form.inputs[0].indices)))
    if isinstance(form, Variable):
        return SYMBOL(bvars.id((form.name, *form.indices)))
    if form.is_one():
        return TRUE
    if form.is_zero():
        return FALSE
    else:
        raise ValueError("Unexpected input in pyeda expression")


def qbf_from_pyeda_int(form):
    """

    Parameters
    ----------
    form : pyeda.boolalg.expr.Expression

    """
    if isinstance(form, AndOp):
        return AND(*[qbf_from_pyeda_int(inp) for inp in form.xs])
    if isinstance(form, OrOp):
        return OR(*[qbf_from_pyeda_int(inp) for inp in form.xs])
    if isinstance(form, NotOp):
        return NOT(qbf_from_pyeda_int(form.xs[0]))
    if isinstance(form, Complement):
        assert len(form.inputs[0].indices) == 1
        return SYMBOL(-form.inputs[0].indices[0])
    if isinstance(form, Variable):
        assert len(form.indices) == 1
        return SYMBOL(form.indices[0])
    if form.is_one():
        return TRUE
    if form.is_zero():
        return FALSE
    else:
        raise ValueError("Unexpected input in pyeda expression")


def oracle_to_minimal_qbf(oracle, *domain_bits):
    all_bits = flatten_to_list(domain_bits)
    if len(set(all_bits)) != len(all_bits):
        raise ValueError("The name of the variables must be unique")

    domains = [range(2 ** len(bits)) for bits in domain_bits]
    tt_out = (oracle(t) for t in itertools.product(*domains))

    # Warning - pyeda apparently doesn't respect the bit order, it sorts them internally so reversing has no effect in espresso_tts
    # So the following doesn't work
    #tt_in = [ttvar('v', index=b) for b in all_bits]
    # correct bit order to match iteration in tt_out (msb first)
    #tt_in = list(reversed(tt_in))

    tt_in = [ttvar('v', index=i+1) for i, _ in enumerate(all_bits)]
    # reverse bit order
    bit_subs_map = {i+1: b for i, b in enumerate(reversed(all_bits))}

    tt = truthtable(tt_in, tt_out)
    # find an approximately minimal Boolean expression for the given truth table
    (fm,) = espresso_tts(tt)
    # convert this expression to our format
    set_expr = qbf_from_pyeda_int(fm)

    # Substitute correct bit names
    set_expr = set_expr.substitute(bit_subs_map)
    return set_expr
