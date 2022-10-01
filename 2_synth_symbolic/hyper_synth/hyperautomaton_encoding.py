import logging
from abc import ABC, abstractmethod

from hyper_synth.automata_encoding import AutomatonEncoding, ControllerEncoding
from hyper_synth.encoding import (BitVectorFunction, ConcreteEncoding,
                                  Encoding, ProductEncoding, SetEncoding)
from hyper_synth.qbf import AND, EXISTS, FORALL, IMPLIES, flatten_to_list

# Explicit -> construct explicit hyperplant, ignore initial state in acceptance condition
# Symbolic -> encode plant, hyperautomaton as automaton, substitute plant path labels into hyperautomaton acceptance

class HyperPlantEncoding(ABC):

    def __init__(self, hyperautomaton, plant_encoding):
        self.hyperautomaton = hyperautomaton
        self.plant_encoding = plant_encoding
        self.logger = logging.getLogger(__name__)

    def accept_form(self, path_length):
        """
        Encode the hyperautomaton specification over the controller as a QBF
        """
        # variables for plant paths
        # indexed by quantifier alternation level and then the index in the level
        path_vars_tuple = tuple(tuple(self.plant_encoding.state_path_vars(path_length) for i in range(level_num_quants))
                                for level_num_quants in self.hyperautomaton.quantifiers)
        form = self.accept_path_tuple_form(flatten_to_list(path_vars_tuple))
        self.logger.debug(f"Hyperautomaton inner acceptance formula size: {form.size()}")

        quant_vs_seq_pairs = zip(self.hyperautomaton.quantifiers, path_vars_tuple)
        # build qbf by iterating through hyperautomaton quantifiers inside-out (i.e., in reversed order)
        for level, (num_paths, level_path_vars) in reversed(list(enumerate(quant_vs_seq_pairs))):
            # TODO - we can reduce the number of occurrences of the `tau` formula by sharing them between quantifiers appropriately
            #    For example, if the quantifiers are forall forall, then we can have one formula `is_paths(p_vars1, p_vars2)`
            #    that represents both path variables encoding a valid path, with only one occurrence of `tau`

            # Even quantifier levels are universal, odd are existential
            path_forms = [self.plant_encoding.path_form(p_vars) for p_vars in level_path_vars]
            if path_forms:
                self.logger.debug(f"Path formula size: {path_forms[0].size()}")
            flat_path_vars = flatten_to_list(flatten_to_list(level_path_vars))
            if level % 2 == 0:
                if num_paths > 0:
                    form = IMPLIES(AND(*path_forms), form)
                    form = FORALL(flat_path_vars, form)
            else:
                form = AND(*path_forms, form)
                form = EXISTS(flat_path_vars, form)

        return form

    # TODO - add option to do disjunction over q instead of quantifiying
    @abstractmethod
    def accept_path_tuple_form(self, vs_seq_tuple):
        """
        Formula satisfied by encodings of a tuple of plant paths which when zipped are
        accepted by the hyperautomaton (when viewed as a word automaton).
        Created by existentially quantifying over accepting hyperautomaton paths.

        Parameters
        ----------
        vs_seq_tuple : list[list[list[int]]]
            Variables encoding plant path for each copy in self-composition
        """


class _ExplicitHyperPlantStateEncoding(ConcreteEncoding):

    def __init__(self, hyperautomaton, hyperplant, plant_state_encoding, hyper_state_encoding):
        self.self_comp_enc = ProductEncoding(*([plant_state_encoding] * hyperautomaton.num_quantifiers))
        self.prod_encoding = ProductEncoding(self.self_comp_enc, hyper_state_encoding)
        self.hyperplant = hyperplant
        num_bits = self.prod_encoding.num_bits
        super().__init__(num_bits)

    def encode(self, s):
        #return self.prod_encoding.encode(self.hyperplant.vs[s]["name"])
        return self.prod_encoding.encode(s)


class ExplicitHyperPlantEncoding(AutomatonEncoding, HyperPlantEncoding):

    # states of hyperplant are of the form (s_1, ..., s_n, q)
    def __init__(self, hyperautomaton, plant_encoding, hyper_state_encoding=None,
                 quantify_path_steps=False):

        HyperPlantEncoding.__init__(self, hyperautomaton, plant_encoding)
        if hyper_state_encoding is None:
            hyper_state_encoding = SetEncoding(self.hyperautomaton.vs["name"])
        self.hyper_state_encoding = hyper_state_encoding

        self.hyperplant = self.hyperautomaton.product_with_plant(self.plant_encoding.plant)
        if self.hyperplant.ecount() == 0:
            self.logger.warning("Hyperplant (product of self-composed plant and hyperautomaton) is empty.")
        state_encoding = _ExplicitHyperPlantStateEncoding(self.hyperautomaton, self.hyperplant,
                                                          self.plant_encoding.state_encoding,
                                                          self.hyper_state_encoding)
        AutomatonEncoding.__init__(self, plant_encoding.var_pool, self.hyperplant,
                                   state_encoding=state_encoding, use_edge_label=False,
                                   quantify_path_steps=quantify_path_steps)

    def accept_path_tuple_form(self, vs_seq_tuple):
        num_steps = len(vs_seq_tuple[0])
        vq_seq = tuple(self.hyper_state_encoding.get_vars(self.var_pool) for i in range(num_steps))
        vqs_seq = tuple(flatten_to_list(l) for l in zip(*vs_seq_tuple, vq_seq))
        form = EXISTS(flatten_to_list(vq_seq), self.path_form(vqs_seq))

        return form


class SymbolicHyperPlantEncoding(HyperPlantEncoding):

    # states of hyperplant are of the form (s_1, ..., s_n, q)
    def __init__(self, hyperautomaton_encoding, plant_encoding, label_func):
        """

        Parameters
        ----------
        hyperautomaton_encoding : AutomatonEncoding
        plant_encoding : ControllerEncoding
        label_func : BitVectorFunction
        """
        if label_func.num_in_bits != plant_encoding.state_encoding.num_bits:
            raise ValueError("Number of label function input bits and state encoding bits must be equal")
        if hyperautomaton_encoding.automaton.num_quantifiers * label_func.num_out_bits\
                != hyperautomaton_encoding.edge_label_encoding.num_bits:
            raise ValueError("Product of number of quantifiers and label function output bits must be"
                             "qualt to the number of hyperautomaton edge label encoding bits")
        super().__init__(hyperautomaton_encoding.automaton, plant_encoding)
        self.hyperautomaton_encoding = hyperautomaton_encoding
        self.label_func = label_func

    def accept_path_tuple_form(self, vs_seq_tuple):
        path_length = len(vs_seq_tuple[0])
        vq_seq = self.hyperautomaton_encoding.state_path_vars(path_length)
        vl_seq = tuple(flatten_to_list([self.label_func(vs) for vs in vs_tuple])
                       for vs_tuple in zip(*vs_seq_tuple))

        form = self.hyperautomaton_encoding.path_form(vq_seq, vl_seq)
        form = EXISTS(flatten_to_list(vq_seq), form)
        return form
