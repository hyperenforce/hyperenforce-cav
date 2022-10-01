import itertools

from hyper_synth.controller_synthesis import (ControllerSynthesisEncoding,
                                              HyperAutomatonEncoding)
from hyper_synth.sat import SATSolver
from pysat.formula import CNF


class ControllerSynthesisEncodingSAT(ControllerSynthesisEncoding):

    def __init__(self, plant, *hyperautomata):
        super().__init__(plant, *hyperautomata)

        if not plant.is_tree():
            raise ValueError("The plant for the SAT controller synthesis encoding must be a tree.")

        self.leaf_indices = self.plant.vs.select(_outdegree=0).indices

        self.true_var = self.bvars.id("True")
        self.false_var = -self.true_var

        self.cnf = None

    def encode(self):

        self.cnf = CNF()
        self.cnf.append([self.true_var])

        self.add_clauses(self.initialization_clauses())
        self.add_clauses(self.no_deadlocks_clauses())
        self.add_clauses(self.reachability_clauses())

        for h in self.hyperautomata:
            h_enc = HyperAutomataEncodingSAT(h, self, self.controller_variables)
            h_enc.encode()
            self.add_clauses(h_enc.clauses)

    def solve(self):
        """
        Solve the encoded SAT instance

        Returns
        -------
        result : list[int] or None
            The list of variable assignments as integers satisfying the formula if one exists, otherwise None
        """
        if self.cnf is None:
            raise RuntimeError("Cannot solve problem before encoding")

        solver = SATSolver(self.cnf)
        return solver.solve()

    def tau(self, e):
        if e["label"] in self.plant.Euc:
            return self.true_var
        return self.controller_tran_var(e)

    def rho(self, s):
        if s in self.plant.vs.indices:
            return self.bvars.id(s)
        else:
            return self.false_var

    def add_clause(self, clause):
        clause = [atom for atom in clause if atom != self.false_var]
        if clause and self.true_var not in clause:
            self.cnf.append(clause)

    def add_clauses(self, clauses):
        for clause in clauses:
            self.add_clause(clause)

    def initialization_clauses(self):
        # Initialization
        s0 = self.plant.initial_state_index
        clauses = [[self.rho(s0)]]
        return clauses

    def no_deadlocks_clauses(self):
        clauses = []
        for s in self.plant.vs.indices:
            clauses.append([self.tau(e) for e in self.plant.es.select(_source=s)])
        return clauses

    def reachability_clauses(self):
        # Reachability in plant
        clauses = []
        for e in self.plant.es:
            clauses.append([-self.rho(e.source), -self.tau(e), self.rho(e.target)])
        return clauses

    # Tseytin transformation to handle conjunction in consequent to put in CNF
    def consequent_var(self, sc):
        return self.bvars.id((sc, 'consequent'))


class HyperAutomataEncodingSAT(HyperAutomatonEncoding):

    def __init__(self, hyperautomaton, parent, vc):
        super().__init__(hyperautomaton, parent, vc)
        # for now, vc must be parent's controller variables
        assert vc is parent.controller_variables
        self.clauses = None

    def encode(self):
        self.clauses = []

        # Linear specification (forall^*)
        if len(self.h.quantifiers) == 1:
            for su in itertools.product(*([self.parent.leaf_indices] * self.h.quantifiers[0])):
                if not any(su == ss for (ss, q) in self.hyper_plant.vs["name"]):
                    self.clauses.append([-self.parent.rho(s) for s in su])
        # Hyper specification (forall^* exists^*)
        elif len(self.h.quantifiers) == 2:
            all_consequents = set()
            for su in itertools.product(*([self.parent.leaf_indices] * self.h.quantifiers[0])):
                consequents = {tuple(sq[0][self.h.quantifiers[0]:]) for sq in self.hyper_plant.vs["name"] if
                               tuple(sq[0][:self.h.quantifiers[0]]) == su}
                all_consequents |= consequents
                self.clauses.append([-self.parent.rho(s) for s in su] + [self.parent.consequent_var(sa) for sa in consequents])
            for sa in all_consequents:
                for s in sa:
                    self.clauses.append([-self.parent.consequent_var(sa), self.parent.rho(s)])
                self.clauses.append([-self.parent.rho(s) for s in sa] + [self.parent.consequent_var(sa)])
        else:
            raise NotImplemented("Only forall*.exist*. quantifiers are supported now")

        return self.clauses
