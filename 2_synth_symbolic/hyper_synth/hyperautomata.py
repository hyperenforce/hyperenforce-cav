from abc import ABC
from inspect import signature

from hyper_synth.automata import Automaton, Plant, SelfComposedPlant
from hyper_synth.compose import generic_sync_compose
from hyper_synth.qbf import QBF


class HyperAutomaton(Automaton, ABC):

    def __init__(self, quantifiers, label_type, **kwargs):
        """

        Parameters
        ----------
        quantifiers : tuple[int]
        """
        super().__init__(**kwargs)
        self.label_type = label_type
        if not all(quant >= 0 for quant in quantifiers):
            raise ValueError("Invalid quantifier specification")
        self.quantifiers = quantifiers

    @property
    def num_quantifiers(self):
        return sum(self.quantifiers)


class ExplicitHyperAutomaton(HyperAutomaton):

    def __init__(self, quantifiers, label_type=None, **kwargs):
        super().__init__(quantifiers, label_type, **kwargs)

    def _check_label(self, label):
        if not len(label) == self.num_quantifiers:
            raise ValueError("ExplicitHyperAutomaton edge must be labeled by a tuple values (one for each quantifier)")
        if self.label_type is not None and not all(self.label_type.is_type_of(l) for l in label):
            raise ValueError("Label type mismatch")
        return True

    def add_edge(self, source, target, label, **kwargs):
        assert self._check_label(label)
        super().add_edge(source, target, label, **kwargs)

    def add_edges(self, pair_list, label, **kwargs):
        assert all(self._check_label(l) for l in label)
        super().add_edges(pair_list, label, **kwargs)

    '''
    def construct_padded(self):
        """
        Construct a hyperautomaton accepting plants augmented with termination behavior
        as in `Plant.construct_padded`.

        This is done by adding transitions at every state to a new terminal state with self-loop.
        All of these transitions are labeled by the tuple of termination labels.
        """
        if self.label_type is None:
            raise NotImplementedError("Padding hyperautomata with termination is only supported for those with label types for now")
        padded_type = _construct_padded_type(self.label_type)
        # TODO - use copy instead
        padded = HyperAutomaton(self.quantifiers, label_type=padded_type)
        padded.add_vertices(self.vcount(), init=self.vs["init"], label=self.vs["label"])
        padded.add_edges([(e.target, e.source) for e in self.es], [e["label"] for e in self.es])

        pad_label_tuple = (PAD_VALUE,) * self.order
        pad_vert = padded.add_vertex(init=False).index
        padded.add_edges([(orig_vert, pad_vert) for orig_vert in padded.vs.indices],
                         [pad_label_tuple] * padded.vcount())
        return padded
    '''

    def product_with_plant(self, plant):
        """
        Construct the product of the hyperautomaton with the self-composition of the given plant.
        The result is the automaton with states named as the tuple of the self-composed state and hyperautomaton state.
        """
        if self.label_type != plant.label_type:
            raise ValueError("Mismatch in plant and hyperautomaton label type")

        comp_plant = plant.self_composition(num_copies=self.num_quantifiers)
        pc0 = comp_plant.initial_state
        initial_hyper_edges = self.es.select(_source_in=self.initial_state_indices, label=pc0["label"])
        init = [(pc0.index, e.target) for e in initial_hyper_edges]

        state_attr_list = {'init', 'marked', 'name'}

        def state_attr_map(gs, hs):
            return {'marked': hs['marked'],
                    'init': (gs.index, hs.index) in init,
                    'name': (gs["name"], hs["name"])}

        def edge_map(ge, he):
            return ge.target_vertex["label"] == he["label"], ''

        hyper_plant = Automaton()
        generic_sync_compose(init, state_attr_list, state_attr_map, edge_map,
                             comp_plant, self, dest=hyper_plant)
        return hyper_plant


class SymbolicHyperAutomaton(HyperAutomaton):

    def __init__(self, quantifiers, label_type, label_encoding, **kwargs):
        super().__init__(quantifiers, label_type, **kwargs)
        self.label_encoding = label_encoding

    def _check_label(self, label):
        #if not isinstance(label, QBF):
        #    raise ValueError("SymbolicHyperAutomaton edge must be labeled by QBF")
        if not callable(label):
            raise ValueError("SymbolicHyperAutomaton edge must be labeled by callable"
                             "mapping edge label encoding to a QBF")
        params = signature(label).parameters
        if not len(params) == self.num_quantifiers and\
           not any(p.kind is p.VAR_POSITIONAL for p in params.values()):
            raise ValueError("Symbolic edge label has the wrong number of arguments.\n")
        return True

    def add_edge(self, source, target, label, **kwargs):
        assert self._check_label(label)
        super().add_edge(source, target, label, **kwargs)

    def add_edges(self, pair_list, label, **kwargs):
        assert all(self._check_label(l) for l in label)
        super().add_edges(pair_list, label, **kwargs)
