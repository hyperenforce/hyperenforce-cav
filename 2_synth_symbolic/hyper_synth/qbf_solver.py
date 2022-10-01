import logging
import os
import os.path
import subprocess
from enum import Enum, auto
from tempfile import TemporaryDirectory
from time import time

import aiger
from dotenv import load_dotenv
from hyper_synth.sat import SolverOutput


class QBFPrenexMode(Enum):
    NONPRENEX = auto()
    PYTHON = auto()
    QCIR2QCIR = auto()


class QBFSolverType(Enum):
    QUABS = auto()
    CAQE = auto()


class QBFSolverCertificateType(Enum):

    def __init__(self, eid, quabs_option, caqe_option):
        self.eid = eid
        self.quabs_option = quabs_option
        self.caqe_option = caqe_option

    AIGER = auto(), "-c", None
    ASSIGNMENT = auto(), "--partial-assignment", "--qdo"


class QBFSolverOutput(SolverOutput):

    def __init__(self):
        super().__init__()
        self.process_data = None
        self.certificate = None
        self.qcir_str = None
        self.qdimacs_str = None


class DirectoryManagerWrapper(str):

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True


class QBFSolver:
    """
    """
    def __init__(self, solver_name=QBFSolverType.QUABS, simplify=True, prenex_mode=QBFPrenexMode.PYTHON, preprocessing=False,
                 tmp_dir_path=None, certifcate_type=QBFSolverCertificateType.ASSIGNMENT, free_as_existential=True,
                 save_qcir=True, save_qdimacs=True, verbose=False, num_threads=None):
        """

        Parameters
        ----------
        solver_name :
        simplify :
        to_prenex :
        tmp_dir_path :
        aiger_certificate : bool
            If True, extract the solution from the Aiger certificate.
            If Fales, extract the solution from the partial assignment.
        """

        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug("Initializing QBF solver.")

        self.solver = solver_name
        if not isinstance(self.solver, QBFSolverType):
            raise ValueError("Unsupported QBF solver.")

        self.simplify = simplify
        self.prenex_mode = prenex_mode
        self.preprocessing = preprocessing

        self.tmp_dir_path = tmp_dir_path

        self.certifcate_type = certifcate_type
        self.free_as_existential = free_as_existential
        self.save_qcir = save_qcir
        self.save_qdimacs = save_qdimacs
        if verbose:
            raise NotImplementedError()
        self.verbose = verbose
        self.num_threads = num_threads

        self.quabs_dir = None
        self.caqe_dir = None
        self.use_wsl = None

    def solve(self, qbf, free_vars):
        """
        Parameters
        ----------
        qbf :
        free_vars : set[int]
            The variables whose values should be extracted from the solution

        """
        self.logger.debug("Solving QBF.")

        self._load_env()
        start_time = time()
        expr = qbf

        qcir_str = None
        qdimacs_str = None

        self.logger.debug("Simplifying QBF")
        # QUABS has trouble with some formulas not in negation normal form or prenex normal form
        if self.prenex_mode is QBFPrenexMode.PYTHON:
            expr = expr.to_prenex()
        if self.simplify:
            expr = expr.to_simplified()

        with DirectoryManagerWrapper(self.tmp_dir_path) if self.tmp_dir_path\
                else TemporaryDirectory() as tmp_dir:
            qcir_path = os.path.join(tmp_dir, "tmp.qcir")

            self.logger.debug("Exporting QBF to qcir")
            mod_qcir_path, qcir_str = self._to_qcir(expr, qcir_path, free_vars)

            if self.solver is QBFSolverType.QUABS:
                self.logger.debug("Solving QBF with QUABS")
                certificate_opt = self.certifcate_type.quabs_option
                # Run quabs command line interface on QCIR file and capture output
                preprocess_val = "1" if self.preprocessing else "0"
                verbose_opts = ["-v"] if self.verbose else []
                num_threads_opts = ["--num-threads", str(self.num_threads)] if self.num_threads is not None else []
                try:
                    process_data = subprocess.run([os.path.join(self.quabs_dir, "quabs").replace("\\", "/"),
                                                   *num_threads_opts, *verbose_opts, certificate_opt, "--preprocessing", preprocess_val, mod_qcir_path],
                                                  capture_output=True, shell=self.windows_os, text=True)
                except FileNotFoundError:
                    raise RuntimeError("`quabs` command not found.\n"
                                       "Did you add it to your path or set the `HYPER_ENF_QUABS_DIR` environment variable?")
                solver_output = self._extract_quabs_solution(process_data, free_vars)

            elif self.solver is QBFSolverType.CAQE:
                self.logger.debug("Solving QBF with CAQE")
                qdimacs_path = os.path.join(tmp_dir, "tmp.qdimacs")
                mod_qdimacs_path, qdimacs_str = self._qcir_to_qdimacs(mod_qcir_path, qdimacs_path)
                certificate_opt = self.certifcate_type.caqe_option
                # Run caqe command line interface on QDIMACS file and capture output
                try:
                    process_data = subprocess.run([os.path.join(self.caqe_dir, "caqe").replace("\\", "/"),
                                                   certificate_opt, mod_qdimacs_path],
                                                  capture_output=True, shell=self.windows_os, text=True)
                except FileNotFoundError:
                    raise RuntimeError("`caqe` command not found.\n"
                                       "Did you add it to your path or set the `HYPER_ENF_CAQE_DIR` environment variable?")
                solver_output = self._extract_caqe_solution(process_data, free_vars)

        end_time = time()
        solver_output.solver_time = (start_time - end_time)
        solver_output.qcir_str = qcir_str
        solver_output.qdimacs_str = qdimacs_str
        return solver_output

    def _load_env(self):
        # load quabs configuration from environment variables or .env file
        self.logger.debug("Loading solver info from environment")
        load_dotenv()
        self.quabs_dir = os.getenv("HYPER_ENF_QUABS_DIR", "")
        self.caqe_dir = os.getenv("HYPER_ENF_CAQE_DIR", "")
        self.use_wsl = int(os.getenv("HYPER_ENF_WSL", "0"))
        self.windows_os = (os.name == 'nt')

    def _modify_path(self, path):
        # If using wsl, convert Windows path to WSL path
        if self.use_wsl:
            # TODO - add error checking
            mod_path = str(subprocess.run(["wsl", "wslpath", "-u", os.path.abspath(path).replace("\\", "/")],
                                               capture_output=True, text=True).stdout.strip())
            if mod_path == "":
                raise RuntimeError("Could not use wsl to translate paths")
        else:
            mod_path = path
        return mod_path

    def _to_qcir(self, expr, qcir_path, free_vars):
        # export formula to .qcir file
        # TODO fix line endings for cross-platform
        with open(qcir_path, "w+", newline="\n") as f:
            expr.to_qcir(f, free_vars, free_as_existential=self.free_as_existential)

        mod_qcir_path = self._modify_path(qcir_path)

        if self.prenex_mode is QBFPrenexMode.QCIR2QCIR or self.preprocessing:
            # Convert to prenex normal form and/or preprocess using qcir2qcir command line interface
            # The solver has better support for solving non-prenex formulas
            # Preprocessing may change the variable names, which prevents extracting a solution :(
            self.logger.debug("Using qcir2qcir for QBF preprocessing")
            options = ["--flatten"]
            if self.prenex_mode is QBFPrenexMode.QCIR2QCIR:
                options += ["--prenexing"]
            if self.preprocessing:
                options += ["--preprocess"]
            # TODO - add error checking
            try:
                qcir_process_data = subprocess.run([os.path.join(self.quabs_dir, "qcir2qcir").replace("\\", "/")] +
                               options + [mod_qcir_path, mod_qcir_path],
                               capture_output=True, shell=self.windows_os, text=True)
                if qcir_process_data.stderr == "":
                    raise RuntimeError("Error using qcir2qcir")

            except FileNotFoundError:
                raise RuntimeError("`qcir2qcir` command not found.\n"
                                   "Did you add it to your path or set the `HYPER_ENF_QUABS_DIR` environment variable?")

        qcir_str = None
        if self.save_qcir:
            with open(qcir_path, "r", newline="\n") as f:
                qcir_str = f.read()
                self.logger.debug(f"QCIR file length: {len(qcir_str)}")

        return mod_qcir_path, qcir_str

    def _qcir_to_qdimacs(self, mod_qcir_path, qdimacs_path):
        self.logger.debug("Transforming qcir to qdimacs")
        self.logger.warning("Transformation to qdimacs may halt execution")
        # translate .qcir file to .qdimacs file
        mod_qdimacs_path = self._modify_path(qdimacs_path)

        # TODO - add error checking
        with open(qdimacs_path, 'w+') as f_qdimacs:
            try:
                subprocess.run([os.path.join(self.quabs_dir, "qcir2qdimacs").replace("\\", "/")] +
                                       [mod_qcir_path], stdout=f_qdimacs,
                                       shell=self.windows_os, text=True)
            except FileNotFoundError:
                raise RuntimeError("`qcir2qdimacs` command not found.\n"
                                   "Did you add it to your path or set the `HYPER_ENF_QUABS_DIR` environment variable?")

        qdimacs_str = None
        if self.save_qdimacs:
            with open(qdimacs_path, "r", newline="\n") as f:
                qdimacs_str = f.read()

        return mod_qdimacs_path, qdimacs_str

    def _extract_quabs_solution(self, process_data, free_vars):
        """
        Extract a solution from the results of solving a QBF.
        The solution is given as the variables in the outermost existential quantifier (or free variables)
        of the QBF that are assigned true.

        Parameters
        ----------
        process_data : CompletedProcess

        Returns
        -------
        true_variables : list[int]
            The variables assigned true
        """
        self.logger.debug("Extracting QBF solution from QUABS output")

        solver_output = QBFSolverOutput()
        solver_output.process_data = process_data

        if not process_data.stdout or process_data.stdout.startswith("error") or process_data.stderr:
            solver_output.msg = "Quabs error: could not process Quabs output"
            self.logger.warning("Quabs error: could not process Quabs output")

        elif "UNSAT" in process_data.stdout:
            solver_output.is_sat = False
            self.logger.debug("UNSAT: Model not found for QBF")

        elif self.certifcate_type is QBFSolverCertificateType.AIGER:
            self.logger.debug("Using Aiger certificate")
            raise NotImplementedError("Aiger certificate not tested")
            # Parse output to aiger representing assignment
            solver_output.certificate = process_data.stdout[process_data.stdout.index("aag"):]
            solution_aag = aiger.parse(solver_output.certificate)
            # Extract variables assigned true from aiger circuit
            solver_output.model = [v for v in free_vars if solution_aag.node_map[str(v)].is_true]
            solver_output.is_sat = True
            # solver_output.solution = [v for v in range(1, self.max_var) if solution_aag.node_map[str(v)].is_true]

        elif self.certifcate_type is QBFSolverCertificateType.ASSIGNMENT:
            self.logger.debug("Using assignment certificate")
            for line in process_data.stdout.splitlines():
                # variable assignment from outer most quantifier
                if line.startswith("V "):
                    # only keep positive values corresponding to true variables
                    solver_output.certificate = line
                    #solver_output.model = {int(v) for v in line.split(" ")[1:]} & set(free_vars)
                    solver_output.model = {int(v) for v in line.split(" ")[1:]} & set(free_vars)

            if not free_vars:
                self.logger.debug("No free variables in QBF so model is empty")
                solver_output.model = []

            if solver_output.model is None:
                solver_output.msg = "Could not extract solution from partial assignment."
                self.logger.warning("Could not extract solution from assignment certificate.")

            else:
                solver_output.is_sat = True
                self.logger.debug("SAT: Model extracted for QBF")

        return solver_output

    def _extract_caqe_solution(self, process_data, free_vars):
        """
        Extract a solution from the results of solving a QBF.
        The solution is given as the variables in the outermost existential quantifier (or free variables)
        of the QBF that are assigned true.

        Parameters
        ----------
        process_data : CompletedProcess

        Returns
        -------
        true_variables : list[int]
            The variables assigned true
        """
        solver_output = QBFSolverOutput()
        solver_output.process_data = process_data

        if not process_data.stdout or process_data.stdout.startswith("error") or process_data.stderr:
            solver_output.msg = "CAQE error: could not process CAQE output"
            self.logger.warning("CAQE error: could not process CAQE output")

        elif "Unsatisfiable" in process_data.stdout:
            solver_output.is_sat = False
            self.logger.debug("UNSAT: Model not found for QBF")

        elif self.certifcate_type is QBFSolverCertificateType.AIGER:
            raise ValueError("Aiger certificate not supported for CAQE solver")

        elif self.certifcate_type is QBFSolverCertificateType.ASSIGNMENT:
            self.logger.debug("Using assignment certificate")
            solver_output.model = set()
            for line in process_data.stdout.splitlines():
                # variable assignments
                solver_output.certificate = ""
                if line.startswith("V "):
                    # only keep positive values corresponding to true variables
                    solver_output.certificate += line + "\n"
                    val = int(line.split(" ")[1])
                    if val > 0 and val in free_vars:
                        solver_output.model.add(val)

            if not free_vars:
                self.logger.debug("No free variables in QBF so model is empty")
                solver_output.model = []
            if solver_output.model is None:
                solver_output.msg = "Could not extract solution from partial assignment."
                self.logger.warning("Could not extract solution from partial assignment.")
            else:
                self.logger.debug("SAT: Model extracted for QBF")
                solver_output.is_sat = True

        return solver_output
