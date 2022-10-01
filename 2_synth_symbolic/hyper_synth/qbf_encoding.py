
import warnings

from hyper_synth.automata_encoding import AutomatonEncoding, ControllerEncoding
from hyper_synth.cardinality_qbf import compare_count_form
from hyper_synth.controller_synthesis import ControllerSynthesisEncoding
from hyper_synth.encoding import ApplicationEncoding
from hyper_synth.hyperautomata import (ExplicitHyperAutomaton,
                                       SymbolicHyperAutomaton)
from hyper_synth.hyperautomaton_encoding import (ExplicitHyperPlantEncoding,
                                                 SymbolicHyperPlantEncoding)
from hyper_synth.qbf import AND, FALSE, FORALL, IMPLIES, NOT, OR, TRUE
from hyper_synth.qbf_io import oracle_to_minimal_qbf
from hyper_synth.qbf_solver import QBFSolver
from hyper_synth.util import SetEncoding, flatten_to_list, to_binary


class ControllerSynthesisEncodingQBF(ControllerSynthesisEncoding):
    """
    Class for encoding the controller synthesis problem as a QBF.

    Attributes
    ----------
    plant : Plant
        The plant to be controlled
    *hyperautomata : list[HyperAutomaton]
        The hyperautomata specifications
    solver : QBFSolver
    plant_state_enc : Encoding
        An encoding of the state indices of the plant
    hyperautomata_state_encs : list[Encoding]
        Encodings for the states indices of each hyperautomaton
    label_enc : ConcreteEncoding
        An encoding of the labels of the plant states
        Only used for symbolic hyperautomata and `label_func` is not provided
    label_func : BitVectorFunction
        Map from plant state encoding to encoding of state label
        Only used for symbolic hyperautomata.
        Generated from `label_enc` if `label_func` is not provided.
    max_depth : int or None
        The maximum length of paths to enforce specifications over
        If None, then it is set to the depth of the graph (number of edges in longest path)
    use_groups : bool
        If True, then use the groups included as the integer attribute "group" on the controllable plant transitions
        In this case, if two transitions have the same group, they must both be enabled or both disabled.
        If they have opposite groups one must be enabled and the other disabled.
    quantify_path_steps: bool
        If True, then create the formulas encoding valid paths of the plant and hyperautomata
        by quantifying over each step rather than conjunction.
        (See equation 2 from
            Dershowitz, N., Hanna, Z., Katz, J. (2005). Bounded Model Checking with QBF.
            In: Bacchus, F., Walsh, T. (eds) Theory and Applications of Satisfiability Testing. SAT 2005.)
    no_deadlocks : bool
        If True, then enforce that there are no deadlocks.
    do_optimization : bool
        If True, then the minimal controller synthesis problem is solved.
        Weights must be given as the nonnegative integer attribute "weight" on the controllable plant transitions
    """

    def __init__(self, plant, *hyperautomata, solver=None,
                 plant_state_enc=None, hyperautomata_state_encs=None,
                 label_enc=None, label_func=None,
                 max_depth=None, use_groups=False,
                 quantify_path_steps=True, no_deadlocks=True,
                 pad_termination=False, do_optimization=False):

        super().__init__(plant, *hyperautomata)
        self.solver = solver
        self.quantify_path_steps = quantify_path_steps
        self.do_optimization = do_optimization
        self.use_groups = use_groups
        self.no_deadlocks = no_deadlocks

        self.cont_enc = ControllerEncoding(self.var_pool, self.plant,
                                           state_encoding=plant_state_enc, use_groups=self.use_groups,
                                           quantify_path_steps=self.quantify_path_steps)
        self.logger.debug(f"Number of controller variables: {len(self.cont_enc.controller_vars)}")

        # Setup plant state label encodings if a hyperautomaton is symbolic
        if any(isinstance(h, SymbolicHyperAutomaton) for h in hyperautomata):
            if label_enc is None and label_func is None:
                label_enc = self.cont_enc.default_label_encoding()
            self.label_enc = label_enc
            if label_func is None:
                label_func = self.cont_enc.default_label_func(self.label_enc)
            self.label_func = label_func

        if hyperautomata_state_encs is not None:
            if len(hyperautomata_state_encs) != len(hyperautomata):
                raise ValueError("Mismatch in number of hyperautomata and hyperautomata state encodings")
        else:
            hyperautomata_state_encs = [None] * len(hyperautomata)
        self.hyperautomata_state_encs = hyperautomata_state_encs


        if pad_termination:
            raise NotImplementedError("Padding not supported for now :(")
            #plant = plant.construct_padded()
            #hyperautomata = [h.construct_padded() for h in hyperautomata]

        if not self.plant.is_dag():
            warnings.warn("The provided plant for QBF controller synthesis is not a DAG."
                          "This may produce unexpected results.")


        if max_depth is None:
            max_depth = self.plant.diameter()
        if max_depth < 1:
            raise ValueError("Depth of plant must be at least 1")
        self.max_depth = max_depth

        self.qbf = None

    def encode(self):
        """
        Create the encoding of the controller synthesis problem.
        Must be called before `solve`.
        """
        self.logger.debug("Encoding controller synthesis problem as QBF")
        if self.do_optimization:
            aux_cont_enc = ControllerEncoding(self.var_pool, self.plant,
                                              state_encoding=self.cont_enc.state_encoding, use_groups=self.use_groups,
                                              quantify_path_steps=self.quantify_path_steps)
            self.qbf = self.controller_form(self.cont_enc) &\
                       FORALL(list(set(aux_cont_enc.group_to_var.values())), IMPLIES(
                              self.controller_form(aux_cont_enc),
                              self.less_controller_cost_form(self.cont_enc, aux_cont_enc)
                       ))
        else:
            self.qbf = self.controller_form(self.cont_enc)

        self.logger.debug(f"Overall controller synthesis QBF size: {self.qbf.size()}")

    def solve(self):
        """
        Solve the encoding of the controller synthesis problem.

        Returns
        -------
        solver_output : QBFSolverOutput
            The output from the QBF solver containing a solution/model if one was found.
        """
        self.logger.debug("Solving controller synthesis problem as QBF")
        if self.qbf is None:
            raise RuntimeError("Cannot solve problem before encoding")
        if self.solver is None:
            solver = QBFSolver()
        else:
            solver = self.solver
        return solver.solve(self.qbf, set(self.cont_enc.group_to_var.values()))

    def decode_cont_trans(self, model):
        edges = []
        controller_vars = self.cont_enc.group_to_var.values()
        solution_map = {vc: TRUE if vc in model else FALSE for vc in controller_vars}
        for e in self.plant.cont_edges:
            form = self.cont_enc.edge_to_form[e]
            form = form.substitute(solution_map)
            # TODO check if this works
            if form.to_prenex().to_simplified() == TRUE:
                edges.append(e)
        return edges

    def controller_form(self, cont_enc):
        form = AND()
        if self.no_deadlocks:
            deadlock_form = self.no_deadlock_form(cont_enc)

            self.logger.debug(f"Deadlock formula size: {deadlock_form.size()}")
            form.add_args(deadlock_form)

        for h, h_state_enc in zip(self.hyperautomata, self.hyperautomata_state_encs):
            hyperform = self.hyperautomaton_form(h, h_state_enc, cont_enc)
            self.logger.debug(f"Hyperautomata acceptance formula size: {hyperform.size()}")
            form.add_args(hyperform)

        return form

    def no_deadlock_form(self, cont_enc):
        """
        Formula satisfied when the controller has no deadlocked states.
        A state is deadlocked if it has an outgoing transition in the plant, but none in the controller

        Parameters
        ----------
        vc : dict[Edge, int]
            Controller variables
        """
        if len(self.plant.cont_edges) == 0:
            return TRUE
        # No deadlocks
        non_terminal_states = {e.source for e in self.plant.es}
        no_deadlock = AND()
        for s in non_terminal_states:
            outgoing = self.plant.es.select(_source=s)
            controllable = outgoing.select(label_notin=self.plant.Euc)
            if outgoing and len(outgoing) == len(controllable):
                no_deadlock.add_args(OR(*[cont_enc.edge_to_form[e] for e in controllable]))
        if no_deadlock == AND():
            return TRUE
        return no_deadlock

    def less_controller_cost_form(self, cont_enc1, cont_enc2):
        """
        Formula satisfied by encodings of controllers where the cost of the first is less than the second.
        """
        cont_list = list(self.plant.cont_edges)
        if "weight" in self.plant.es.attribute_names():
            costs = [e["weight"] for e in cont_list]
        else:
            costs = None
        # as costs are associated with the absence of a transition,
        # we count the number of controller variables set to false
        vc1_vec = tuple(NOT(cont_enc1.edge_to_form[e]) for e in cont_list)
        vc2_vec = tuple(NOT(cont_enc2.edge_to_form[e]) for e in cont_list)
        return compare_count_form(vc1_vec, vc2_vec, self.var_pool, coeffs1=costs, coeffs2=costs)

    def hyperautomaton_form(self, h, h_state_enc, cont_enc):
        if isinstance(h, ExplicitHyperAutomaton):
            hyperplant_enc = ExplicitHyperPlantEncoding(h, cont_enc, hyper_state_encoding=h_state_enc,
                                                        quantify_path_steps=self.quantify_path_steps)
        elif isinstance(h, SymbolicHyperAutomaton):
            edge_label_encoding = ApplicationEncoding(num_args=h.num_quantifiers,
                                                      num_arg_bits=self.label_func.num_out_bits)
            h_enc = AutomatonEncoding(self.var_pool, h,
                                      state_encoding=h_state_enc, edge_label_encoding=edge_label_encoding,
                                      quantify_path_steps=self.quantify_path_steps)
            hyperplant_enc = SymbolicHyperPlantEncoding(h_enc, cont_enc, self.label_func)
        else:
            raise ValueError(f"Unknown hyperautomaton type: {type(h)}")
        return hyperplant_enc.accept_form(self.max_depth)

    def decode_groups(self, solution):
        if solution is None:
            return None
        solution = set(solution)
        return [group for group in self.cont_enc.groups if self.cont_enc.group_to_var[group] in solution]
