import itertools
import math
from collections import namedtuple


class DataType:
    """
    A class representing types given by assignments of variables to given finite domains.

    Given an instance of DataType, we can construct instances of this type as named tuples
    >>> t = DataType({"v1":[1,2,3], "v2":["a", "b"]})
    >>> v = t(v1=2, v2="a")
    >>> print(v)
    datatype(v1=2, v2='a')
    """

    def __init__(self, var_value_dict, default_dict=None):
        """
        Construct a DataType from variable names and corresponding finite domains.

        Parameters
        ----------
        var_value_dict : dict[str:list]
            A map from the variable names of the type to the domain of possible values it can take on
        default_dict : dict[str:obj]
            A map from the variable names to their default values
        """
        # self._var_value_dict = var_value_dict
        self._var_value_dict = {k: frozenset(v) for k, v in var_value_dict.items()}
        self._keys = self._var_value_dict.keys()
        if default_dict is None:
            default_dict = {n: next(iter(vals)) for n, vals in var_value_dict.items()}
        def_tuple = tuple(default_dict[key] for key in default_dict)
        self.TupleClass = namedtuple('datatype', self._keys, defaults=def_tuple)

    def __str__(self):
        return str(tuple(self.var_names()))

    def __call__(self, **kwargs):
        return self.TupleClass(**kwargs)

    def __iter__(self):
        for val in itertools.product(*[self.var_values(name) for name in self.var_names()]):
            yield self.TupleClass._make(val)

    def __eq__(self, other):
        return self._var_value_dict == other._var_value_dict

    def __hash__(self):
        # TODO make sure this is a valid hash
        return hash(frozenset(self._var_value_dict.items()))

    @property
    def default_value(self):
        return self()

    def var_names(self):
        return self._keys

    def var_values(self, name):
        return self._var_value_dict[name]

    def num_values(self):
        return math.prod([len(v) for v in self._var_value_dict.values()])

    def subtype(self, names):
        default_dict = {k: v for k, v in self.default_value._asdict().items() if k in names}
        st = DataType({name: self._var_value_dict[name] for name in names}, default_dict)
        return st

    def is_subtype(self, other):
        for name in self.var_names():
            other_vals = other._var_value_dict.get(name)
            if other_vals is None or not self._var_value_dict[name].issubset(other_vals):
                return False
        return True

    def is_supertype(self, other):
        return other.is_subtype(self)

    def is_disjoint(self, other):
        return self.var_names().isdisjoint(other.var_names())

    def is_type_of(self, val):
        #if not isinstance(val, self.TupleClass):
        #    return False
        if not hasattr(val, "_asdict"):
            return False
        for k, v in val._asdict().items():
            if v not in self.var_values(k):
                return False
        return True

    def projection(self, val):
        return self.TupleClass(**{k: v for k, v in val._asdict().items() if k in self.var_names()})

    def inverse_projection(self, val):
        val_dict = val._asdict()
        new_names = list(self.var_names() - val_dict.keys())
        other_values = itertools.product(*[self.var_values(name) for name in new_names])
        return {self.TupleClass(**(val_dict | dict(zip(new_names, o_val)))) for o_val in other_values}

    def inverse_projection_gen(self, val):
        val_dict = val._asdict()
        new_names = list(self.var_names() - val_dict.keys())
        for o_val in itertools.product(*[self.var_values(name) for name in new_names]):
            yield self.TupleClass(**(val_dict | dict(zip(new_names, o_val))))

    def from_subvalues(self, *subvalues):
        return self(**{k: v for sv in subvalues for k, v in sv._asdict().items()})

    def product_type(self, *others):
        var_value_dict = {}
        var_value_dict |= self._var_value_dict
        default_dict = self.default_value._asdict()
        for other in others:
            var_value_dict |= other._var_value_dict
            default_dict |= other.default_value._asdict()
        pt = DataType(var_value_dict, default_dict)
        return pt

    def quotient_type(self, subtype):
        if not self.is_supertype(subtype):
            raise ValueError("Can only quotient type by a subtype")
        return self.subtype(self.var_names() - subtype.var_names())

    def stringify(self):
        return DataType({str(key): {str(v) for v in vals}
                         for key, vals in self._var_value_dict.items()})

    def is_empty_type(self):
        return len(self.var_names()) == 0

    def from_ordered_values(self, values):
        if not type(values) == list and not type(values) == tuple:
            values = (values,)
        return self(**dict(zip(self.var_names(), values)))

    def copy_with_new_names(self, name_dict):
        orig_default_dict = self.default_value._asdict()
        default_dict = {v: orig_default_dict[n] for n, v in name_dict.items() if n in self.var_names()}
        copy_type = DataType({name_dict[n]: self.var_values(n) for n in self.var_names()}, default_dict)
        return copy_type


empty_type = DataType({})
empty_value = empty_type()
