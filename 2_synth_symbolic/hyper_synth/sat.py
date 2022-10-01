from abc import ABC

from pysat.solvers import Solver as PySatSolver


class SolverOutput(ABC):

    def __init__(self):
        self.model = None
        self.is_sat = None
        self.msg = None
        self.solver_time = None

    @property
    def is_error(self):
        return self.is_sat is None


class SATSolverOutput(SolverOutput):

    def __init__(self):
        super().__init__()


class SATSolver:

    def __init__(self, cnf, solver_name=None):
        self.cnf = cnf
        self.solver_name = solver_name
        solver_settings = dict()
        if self.solver_name:
            solver_settings["name"] = solver_settings
        self.solver = PySatSolver(**solver_settings, use_timer=True)
        self.solver.append_formula(self.cnf)

    def solve(self):
        self.solver.solve()
        solver_output = SATSolverOutput()
        status = self.solver.get_status()
        if status is None:
            solver_output.msg = "Solver interrupted."
        else:
            solver_output.solver_time = self.solver.time()
            solver_output.model = self.solver.get_model()
            solver_output.is_sat = self.solver.get_model() is None
        # cleanup
        self.solver.delete()
        return solver_output
