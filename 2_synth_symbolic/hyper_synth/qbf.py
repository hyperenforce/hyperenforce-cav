# Expression structure inspired by https://github.com/bastikr/boolean.py

from hyper_synth.util import flatten_to_list

_VariableName = int


def _convert_arg(arg):
    """
    Convert expression like objection into a valid `_Expression`
    """
    if arg is True:
        arg = TRUE
    elif arg is False:
        arg = FALSE
    elif isinstance(arg, _VariableName):
        arg = SYMBOL(arg)
    elif not isinstance(arg, QBF):
        raise ValueError("Invalid argument for expression")
    return arg


class QBF:
    """
    Representation of QBF expressions
    Types of expressions, like AND, OR, FORALL, etc. are created as subclasses.
    """

    def __init__(self, *args):
        self._args = tuple()
        # The maximum index of variables used in this expression
        self.max_var = 0
        self._add_args(*args)
        self.is_literal = False

    def _add_args(self, *args):
        self._args = self._args + tuple(_convert_arg(arg) for arg in args)
        self.max_var = max([self.max_var] + [arg.max_var for arg in self._args])

    def __repr__(self):
        return self.__str__()

    def __or__(self, other):
        return OR(self, other)

    def __and__(self, other):
        return AND(self, other)

    def __invert__(self):
        return NOT(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self._args == other._args

    def __hash__(self):
        # TODO - check valid hash
        return (self.__class__, tuple(self._args)).__hash__()

    def size(self):
        return 1 + sum([child.size() for child in self._args])

    def substitute(self, var_dict):
        """
        Substitute the variables used in this expression according to the dictionary `var_dict`
        Overridden by subclasses
        """
        return self

    def to_simplified(self):
        """
        Construct a simplified version of this expression
        Meant to be overridden by subclasses
        """
        return self

    def to_prenex(self):
        """
        Construct a prenexed version of this expression
        Meant to be overridden by subclasses
        """
        return self

    def to_qcir(self, f, free_vars, free_as_existential=True):
        # import here to avoid circular import dependencies
        from hyper_synth.qbf_io import QCIRWriter
        QCIRWriter(f, self, free_vars, free_as_existential).write()

    @staticmethod
    def from_qcir(f):
        # import here to avoid circular import dependencies
        from hyper_synth.qbf_io import QCIRReader
        return QCIRReader(f).read()

    def find_solution(self, free_vars, **kwargs):
        # import here to avoid circular import dependencies
        from hyper_synth.qbf_solver import QBFSolver
        solver = QBFSolver(**kwargs)
        output = solver.solve(self, free_vars)
        if output.is_error:
            raise RuntimeError("Encountered error when finding solution to qbf.\n", output.msg)
        return output.model


class _TRUE(QBF):

    def __init__(self):
        super().__init__()
        self.is_literal = True
        self.dual = None

    def __str__(self):
        return "T"


class _FALSE(QBF):

    def __init__(self):
        super().__init__()
        self.is_literal = True
        self.dual = None

    def __str__(self):
        return "F"


TRUE = _TRUE()
FALSE = _FALSE()
TRUE.dual = FALSE
FALSE.dual = TRUE


class SYMBOL(QBF):

    def __init__(self, var):
        """

        Parameters
        ----------
        var : int
        """
        super().__init__()
        self.is_literal = True

        assert isinstance(var, _VariableName) and var != 0
        self.var = var
        self.max_var = abs(var)

    @property
    def dual(self):
        return SYMBOL(-self.var)

    def __hash__(self):
        return self.var.__hash__()

    def __eq__(self, other):
        return super().__eq__(other) and self.var == other.var

    def __str__(self):
        return str(self.var)

    def substitute(self, var_dict):
        if self.var in var_dict:
            return _convert_arg(var_dict[self.var])
        if -self.var in var_dict:
            return NOT(_convert_arg(var_dict[-self.var]))
        return self


class _Function(QBF):

    def __init__(self, *args):
        super().__init__(*args)
        self.operator = None

    def substitute(self, var_dict):
        return self.__class__(*[arg.substitute(var_dict) for arg in self._args])


class _AndOr(_Function):

    def __init__(self, *args):
        super().__init__(*args)
        self.dual = None
        self.annihilator = None
        self.identity = None

    def __str__(self):
        return f"{self.operator}({', '.join(str(arg) for arg in self._args)})"

    def add_args(self, *args):
        self._add_args(*args)

    def to_simplified(self):
        if not self._args:
            raise ValueError("And/Or with no arguments are not well-defined")
        args = tuple(arg.to_simplified() for arg in self._args)
        unique_args = []
        for arg in args:
            if arg not in unique_args:
                unique_args.append(arg)
        args = tuple(arg for arg in unique_args if arg != self.identity)
        if not args:
            return self.identity
        if self.annihilator in args:
            return self.annihilator
        if len(args) == 1:
            return args[0]
        return self.__class__(*args)

    def to_prenex(self):
        if not self._args:
            raise AttributeError("And/Or with no arguments are not well-defined")

        args = tuple(arg.to_prenex() for arg in self._args)
        if len(args) == 1:
            return args[0]

        exists_args = [arg.quant_expr for arg in args if isinstance(arg, EXISTS)]
        exists_vars = flatten_to_list([arg.quant_variables for arg in args if isinstance(arg, EXISTS)])
        forall_args = [arg.quant_expr for arg in args if isinstance(arg, FORALL)]
        forall_vars = flatten_to_list([arg.quant_variables for arg in args if isinstance(arg, FORALL)])
        unquant_args = [arg for arg in args if not isinstance(arg, _Quantification)]
        form = self.__class__(*exists_args, *forall_args, *unquant_args)

        quant_vars = exists_vars + forall_vars
        if len(quant_vars) != len(set(quant_vars)):
            raise AttributeError("Variables in qbf may only be quantified once.")

        if exists_args:
            form = EXISTS(exists_vars, form)
        if forall_args:
            form = FORALL(forall_vars, form)

        # TODO avoid using recursion to push and/or down a chain of quantifiers
        if any(isinstance(arg, _Quantification) for arg in exists_args + forall_args):
            return form.to_prenex()
        else:
            return form

    @property
    def operands(self):
        return self._args


class AND(_AndOr):

    def __init__(self, *args):
        super().__init__(*args)
        self.dual = OR
        self.operator = "and"
        self.annihilator = FALSE
        self.identity = TRUE


class OR(_AndOr):

    def __init__(self, *args):
        super().__init__(*args)
        self.dual = AND
        self.operator = "or"
        self.annihilator = TRUE
        self.identity = FALSE


class NOT(_Function):

    def __init__(self, arg):
        super().__init__(arg)
        self.operator = "-"

    def __str__(self):
        return f"{self.operator}{str(self._args[0])}"

    @property
    def inner_expr(self):
        return self._args[0]

    def to_simplified(self):

        expr = self
        while isinstance(expr, NOT):
            if isinstance(expr.inner_expr, NOT):
                expr = expr.inner_expr.inner_expr
            else:
                inner = expr.inner_expr.to_simplified()
                if inner.is_literal:
                    return inner.dual
                elif isinstance(inner, _AndOr):
                    expr = inner.dual(*[NOT(arg) for arg in inner._args])
                elif isinstance(inner, _Quantification):
                    expr = inner.dual(inner.quant_variables, NOT(inner.quant_expr))
                else:
                    raise ValueError("This shouldn't be reachable")
                expr = expr.to_simplified()
        return expr.to_simplified()

    def to_prenex(self):
        inner = self.inner_expr.to_prenex()
        if isinstance(inner, _Quantification):
            form = inner.dual(inner.quant_variables, NOT(inner.quant_expr))
        else:
            form = NOT(inner)
        return form


def IMPLIES(assumption, consequent):
    return OR(NOT(assumption), consequent)


def EQUIVALENT(expr1, expr2):
    return AND(IMPLIES(expr1, expr2), IMPLIES(expr2, expr1))


class _Quantification(QBF):

    def __init__(self, quant_variables, inner):
        super().__init__(inner)
        self.quantifier = None
        self.dual = None

        assert all(isinstance(v, _VariableName) and v > 0 for v in quant_variables)
        self.quant_variables = tuple(quant_variables)
        # self.max_var repeated twice in case self.quant_variables is empty
        self.max_var = max(self.max_var, self.max_var, *self.quant_variables)

    @property
    def quant_expr(self):
        return self._args[0]

    def __hash__(self):
        return (self.__class__, tuple(self._args), tuple(self.quant_variables)).__hash__()

    def __eq__(self, other):
        return super().__eq__(other) and self.quant_variables == other.quant_variables

    def __str__(self):
        return f"{self.quantifier}({', '.join(str(v) for v in self.quant_variables)}; {self.quant_expr})"

    def to_simplified(self):
        quant_expr = self.quant_expr.to_simplified()
        if quant_expr in (TRUE, FALSE):
            return quant_expr
        # Flatten repeated quantifiers
        if self.__class__ == quant_expr.__class__:
            return self.__class__(self.quant_variables + quant_expr.quant_variables, quant_expr.quant_expr)
        return self.__class__(self.quant_variables, quant_expr)

    def to_prenex(self):
        quant_expr = self.quant_expr.to_prenex()
        return self.__class__(self.quant_variables, quant_expr)

    def substitute(self, var_dict):
        new_quant_variables = []
        for v in self.quant_variables:
            v = var_dict.get(v, v)
            if not isinstance(v, _VariableName) and v > 0:
                raise ValueError("Can only substitute variables for quantified variables")
            new_quant_variables.append(v)
        return self.__class__(new_quant_variables, self.quant_expr.substitute(var_dict))


class FORALL(_Quantification):

    def __init__(self, quant_variables, inner):
        super().__init__(quant_variables, inner)
        self.quantifier = "forall"
        self.dual = EXISTS

    def to_simplified(self):
        if not self.quant_variables:
            return self.quant_expr.to_simplified()
        return super().to_simplified()

    def to_prenex(self):
        if not self.quant_variables:
            return self.quant_expr.to_prenex()
        return super().to_prenex()


class EXISTS(_Quantification):

    def __init__(self, quant_variables, inner):
        super().__init__(quant_variables, inner)
        self.quantifier = "exists"
        self.dual = FORALL

    def to_simplified(self):
        if not self.quant_variables:
            return FALSE
        return super().to_simplified()

    def to_prenex(self):
        if not self.quant_variables:
            return FALSE
        return super().to_prenex()
