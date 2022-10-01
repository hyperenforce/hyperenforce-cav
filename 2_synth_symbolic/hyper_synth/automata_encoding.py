import logging

from hyper_synth.automata import Automaton, Plant
from hyper_synth.datatype import DataType
from hyper_synth.encoding import (BitVectorFunction, DataTypeEncoding,
                                  SetEncoding, equal_tuple_form)
from hyper_synth.qbf import AND, FALSE, FORALL, IMPLIES, OR, SYMBOL, TRUE


class AutomatonEncoding:
    """
    An encoding of an automaton into QBFs.
    Using encodings of state and edge labels, this class provides methods for creating
    QBFs accepting encodings of paths of the automaton.
    """

    def __init__(self, var_pool, automaton, state_encoding=None, edge_label_encoding=None,
                 use_edge_label=True, quantify_path_steps=False):
        self.var_pool = var_pool
        self.automaton = automaton

        if state_encoding is None:
            state_encoding = SetEncoding(self.automaton.vs["name"])
        self.state_encoding = state_encoding

        self.use_edge_label = use_edge_label
        if self.use_edge_label and edge_label_encoding is None:
            self.edge_label_encoding = SetEncoding(list(set(self.automaton.es["label"])))
        self.edge_label_encoding = edge_label_encoding

        self.quantify_path_steps = quantify_path_steps
        self.logger = logging.getLogger(__name__)

    def state_vars(self):
        return self.state_encoding.get_vars(self.var_pool)

    def edge_label_vars(self):
        if self.use_edge_label:
            return self.edge_label_encoding.get_vars(self.var_pool)
        else:
            return ()

    def state_path_vars(self, length):
        """
        Parameters
        ----------
        length : int
            The number of transitions in the path

        Returns
        -------
        vs_seq : tuple(tuple(int))
            The tuple of state variables
        """
        if length < 0:
            raise ValueError("Path length must be at least 0.")
        return tuple(self.state_vars() for i in range(length + 1))

    def edge_path_vars(self, length):
        """
        Parameters
        ----------
        length : int
            The number of transitions in the path

        Returns
        -------
        vl_seq : tuple(tuple(int))
            The tuple of edge label variables
        """
        if length < 0:
            raise ValueError("Path length must be at least 0.")
        return tuple(self.edge_label_vars() for i in range(length))

    def init_state_form(self, vs):
        """
        Formula satisfied by the encoding of the initial plant state
        """
        return OR(*[self.state_encoding.encodes_form(vs, init_name)
                    for init_name in self.automaton.initial_states["name"]])

    def encodes_edge_form(self, vs, vl, vsp, e):
        form = AND(self.state_encoding.encodes_form(vs, e.source_vertex["name"]),
                   self.state_encoding.encodes_form(vsp, e.target_vertex["name"]))
        if self.use_edge_label:
            form.add_args(self.edge_label_encoding.encodes_form(vl, e["label"]))
        return form

    # TODO - add step hint, allowing us to take advantage of the automata structure in the conjunctive path form
    def trans_form(self, vs, vl, vsp):
        """
        Formula satisfied by encodings of an automaton transitions.

        Parameters
        ----------
        vs : list[int]
            Source state variables
        vsp : list[int]
            Target state variables
        vl : list[int]
            Edge label variables
        """
        form = OR(*[self.encodes_edge_form(vs, vl, vsp, e) for e in self.automaton.es])
        self.logger.debug(f"Number of edges in auto: {self.automaton.ecount()}")
        return form

    def path_form(self, vs_seq, vl_seq=None):
        """
        Formula satisfied by encodings of automaton paths.

        Parameters
        ----------
        vs_seq : list[list[int]]
        vl_seq : list[list[int]] or None
        """

        if len(vs_seq) <= 0:
            raise ValueError("Path length must be at least 1.")

        if vl_seq is None:
            vl_seq = [()] * (len(vs_seq) - 1)
        assert len(vs_seq) == len(vl_seq) + 1

        if len(vs_seq) == 1:
            form = TRUE
        elif self.quantify_path_steps:
            form = self.quantify_steps_path_form(vs_seq, vl_seq)
        else:
            form = self.conjunctive_path_form(vs_seq, vl_seq)

        return AND(self.init_state_form(vs_seq[0]), form)

    def quantify_steps_path_form(self, vs_seq, vl_seq):
        """
        Formula satisfied by encodings of controller paths created by
        universally quantifying over each step, requiring it to encode a controller transition.
        """
        z = self.state_vars()
        zp = self.state_vars()
        zl = self.edge_label_vars()
        trans_form = self.trans_form(z, zl, zp)
        self.logger.debug(f"Transition formula size {trans_form.size()}")
        q_path_form = FORALL(z + zl + zp, IMPLIES(
            OR(*[equal_tuple_form(s, z) & equal_tuple_form(l, zl) & equal_tuple_form(sp, zp)
                 for (s, l, sp) in zip(vs_seq, vl_seq, vs_seq[1:])]),
            trans_form
        ))
        return q_path_form

    def conjunctive_path_form(self, vs_seq, vl_seq):
        """
        Formula satisfied by encodings of controller paths created as
        the conjunction of each step encoding a controller transition.
        """
        return AND(*[self.trans_form(vs, vl, vsp) for vs, vl, vsp in zip(vs_seq, vl_seq, vs_seq[1:])])


class ControllerEncoding(AutomatonEncoding):

    def __init__(self, var_pool, plant, use_groups=False, state_encoding=None, quantify_path_steps=False):
        super().__init__(var_pool, plant, state_encoding=state_encoding, use_edge_label=False,
                         quantify_path_steps=quantify_path_steps)

        self.use_groups = use_groups
        self.groups, self.group_to_var, self.edge_to_form = self._create_controller_vars()

    @property
    def plant(self):
        return self.automaton

    # override explicit formula adding constraint on controllable edges
    def encodes_edge_form(self, vs, vl, vsp, e):
        form = super().encodes_edge_form(vs, vl, vsp, e)
        # Uncontrollable transitions are always included
        # Controllable transitions are included if the corresponding variable is set to true
        if e in self.plant.cont_edges:
            form = AND(form, self.controller_form(e))
        return form

    def _create_controller_vars(self):
        if self.use_groups:
            # use groups specified by edge labels
            groups = {abs(g) for g in self.plant.es["group"]}
            group_to_var = {g: self.var_pool.get_var() for g in groups}
            edge_to_form = {e: SYMBOL(group_to_var[e["group"]]) if e["group"] > 0 else
                               SYMBOL(-group_to_var[-e["group"]])
                            for e in self.plant.cont_edges}
        else:
            # each controllable edge forms its own independent group
            cont_list = list(self.plant.cont_edges)
            groups = list(i+1 for i, e in enumerate(cont_list))
            group_to_var = {g: self.var_pool.get_var() for g in groups}
            edge_to_form = {e: SYMBOL(group_to_var[groups[cont_list.index(e)]])
                            for e in self.plant.cont_edges}
        return groups, group_to_var, edge_to_form

    @property
    def controller_vars(self):
        return list(set(self.group_to_var.values()))

    def controller_form(self, edge):
        return self.edge_to_form[edge]

    def default_label_encoding(self):
        """
        Construct default encoding of state labels.
        Used when states labels have no inherent structure.
        """
        if isinstance(self.plant.label_type, DataType):
            label_enc = DataTypeEncoding(self.plant.label_type)
        else:
            labels = list(set(self.plant.vs["label"]))
            label_enc = SetEncoding(labels)
        return label_enc

    def default_label_func(self, label_enc):
        """
        Construct encoding of map from state encoding to label encoding.
        Used when labels have no inherent structure relative to states.

        Parameters
        ----------
        label_enc : ConcreteEncoding
            Encoding of the state labels to use

        Returns
        -------
        label_func : BitVectorFunction
        """
        plant = self.plant
        plant_state_enc = self.state_encoding
        # TODO use classes from encoding.py
        def label_forms(vss):
            forms = [OR() for i in range(label_enc.num_bits)]
            for s in plant.vs:
                label_bits = label_enc.encode(s["label"])
                for i in [i for i, bit in enumerate(label_bits) if bit]:
                    #forms[i].add_args(plant_state_enc.encodes_form(vss, s.index))
                    forms[i].add_args(plant_state_enc.encodes_form(vss, s["name"]))
            # TODO -> move simplification elsewhere to avoid always simplifying each call

            # In case a bit is not set (it is always False), change the formula to reflect this
            # TODO -> errors like this could be avoided if we choose a convention for the truth of empty AND/OR statements
            forms = [f if f != OR() else FALSE for f in forms]
            return [form.to_simplified() for form in forms]

        return BitVectorFunction(plant_state_enc.num_bits, label_enc.num_bits, label_forms)


'''
def minimized_tau_form(self, vs, vl, vsp):
    """
    Formula satisfied by encodings of a controller transition created using Boolean formula minimization.
    The satisfaction of this formula is arbitrary for transitions not present in the plant.
    """
    """
    # TODO - there appears to be a problem with minimization right now
    #    Does this still have to do with bit order?
    cont_egde_list = list(self.plant.cont_edges)
    tran_var_list = [vc[e] for e in cont_egde_list]

    # subsets of controllable transitions are encoded so the ith bit is true if the ith transition is included
    def has_trans(el, ev):
        # determine if edge literal `el` is included in edge set represented by variable `ev`
        return to_binary(ev, len(cont_egde_list))[cont_egde_list.index(el)]

    # This assumes states are encoded as the binary (big endian) representation of their index
    def oracle(sspe):
        if sspe[0] not in self.plant.vs.indices or sspe[1] not in self.plant.vs.indices:
            return "X"
        es = self.plant.es.select(_source=sspe[0], _target=sspe[1])
        if not es or not (es.select(label_in=self.plant.Euc) or has_trans(es[0], sspe[2])):
            return "0"
        else:
            return "1"

    return oracle_to_minimal_qbf(oracle, vs, vsp, tran_var_list)
    """
'''
