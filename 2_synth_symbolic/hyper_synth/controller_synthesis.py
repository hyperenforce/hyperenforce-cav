import logging
from abc import ABC, abstractmethod

from DESops.basic_operations.unary import find_inacc
from hyper_synth.automata import Plant
from hyper_synth.automata_encoding import ControllerEncoding
from hyper_synth.encoding import VariablePool
from hyper_synth.qbf import FALSE, TRUE


class ControllerSynthesisEncoding(ABC):
    """
    Encode the controller synthesis problem for the given plant and specifications as an instance of QBF SAT.

    Attributes
    ----------
    plant : NFA
        The plant to be controlled
    hyper_automata_and_quants : list[NFA or tuple]
        An alternating list of hyperautomata representing the spec and the corresponding quantifier as a tuple.
        Each number in the quantifier tuple represents the number of sequential quantifiers before the next alternation.
        For example, the first number represents the leading number of universal quantifiers.
        The second number represents the following number of existential quantifiers, and so on.

    """

    # move qbf specifics to qbf subclass
    def __init__(self, plant, *hyperautomata):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug("Initializing controller synthesis encoding.")

        # TODO copy instead of assign?
        self.plant = plant
        # TODO remove this line if possible
        #self.plant.vs["name"] = self.plant.vs.indices

        self.hyperautomata = list(hyperautomata)

        self.var_pool = VariablePool()


    @abstractmethod
    def encode(self):
        pass

    @abstractmethod
    def solve(self):
        pass

    @abstractmethod
    def decode_cont_trans(self, model):
        # returns the set of controllable transitions from a given model
        pass

    def decode_controller(self, model):
        """
        Convert the output from solving to the controller as a subset of the plant.

        Parameters
        ----------
        model : list[int] or None
            The output from solving

        Returns
        -------
        controller : NFA
            The controller plant
        """
        self.logger.debug("Start controller decoding.")
        if model is None:
            self.logger.debug("No controller decoded from no solution.")
            return None

        controller = Plant(label_type=self.plant.label_type)
        controller.add_vertices(self.plant.vcount(), name=self.plant.vs["name"], label=self.plant.vs["label"])
        controller.initial_state_index = self.plant.initial_state_index
        edges = list(self.plant.uncont_edges)

        edges.extend(self.decode_cont_trans(model))

        edge_info = [((e.source, e.target), e["label"]) for e in edges]
        edge_info = tuple(zip(*edge_info))
        controller.add_edges(edge_info[0], edge_info[1])

        controller.delete_vertices(find_inacc(controller))
        self.logger.debug("Controller decoded from solution.")
        return controller
