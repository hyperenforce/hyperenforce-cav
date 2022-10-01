import itertools
import math
from abc import ABC, abstractmethod

from hyper_synth.cardinality_qbf import at_most_k_form
from hyper_synth.datatype import DataType
from hyper_synth.qbf import AND, EQUIVALENT, OR, TRUE
from hyper_synth.util import flatten_to_list, to_binary

"""
An encoding relates an explicit object with its bitvector representation.
"""

class VariablePool:
    """
    Utility class for generating unique variables
    """

    def __init__(self, start_from=1):
        super().__init__()
        self.counter = start_from

    def get_var(self):
        return self.get_vars(1)[0]

    def get_vars(self, num_vars):
        assert num_vars >= 0
        var_tup = tuple(range(self.counter, self.counter + num_vars))
        self.counter += num_vars
        return var_tup


def equal_tuple_form(vt1, vt2):
    if len(vt1) != len(vt2):
        raise ValueError("Cannot compare tuples of different lengths")
    if len(vt1) == 0:
        return TRUE
    return AND(*[EQUIVALENT(v1, v2) for v1, v2 in zip(vt1, vt2)])


class Encoding(ABC):
    """
    A Boolean encoding of a set of values

    Attributes
    -------
    num_bits : int
        The number of bits used
    """

    def __init__(self, num_bits):
        self.num_bits = num_bits

    def get_vars(self, var_pool):
        return var_pool.get_vars(self.num_bits)

    @abstractmethod
    def encodes_form(self, vs, s):
        pass


class ConcreteEncoding(Encoding):
    def __init__(self, num_bits):
        super().__init__(num_bits)

    @abstractmethod
    def encode(self, s):
        pass

    def encodes_form(self, vs, s):
        return equal_tuple_form(self.encode(s), vs)


class SetEncoding(ConcreteEncoding):

    def __init__(self, vals):
        """
        Construct a Boolean encoding of a set of values.

        Parameters
        ----------
        vals : list[obj]
        """
        if len(vals) != len(set(vals)):
            raise ValueError("Values must be unique")
        self.vals = list(vals)
        num_bits = math.ceil(math.log2(len(self.vals)))
        self.to_bits = {val: to_binary(i, num_bits) for i, val in enumerate(self.vals)}
        self.from_bits = {v: k for k, v in self.to_bits.items()}
        super().__init__(num_bits)

    def encode(self, s):
        return self.to_bits[s]


class ProductEncoding(ConcreteEncoding):

    def __init__(self, *encodings):
        self.encodings = encodings
        num_bits = sum(enc.num_bits for enc in self.encodings)
        super().__init__(num_bits)

    def encode(self, s):
        assert len(s) == len(self.encodings)
        return tuple(flatten_to_list([enc.encode(sv) for sv, enc in zip(s, self.encodings)]))

    def encodes_component_form(self, vs, s, index):
        return self.encodings[index].encodes_form(vs, s)


class DataTypeEncoding(ConcreteEncoding):

    def __init__(self, data_type):
        self.data_type = data_type
        self.var_names = list(data_type.var_names())
        self.var_enc_dict = {name: SetEncoding(data_type.var_values(name)) for name in data_type.var_names()}
        offset = 0
        self.var_bit_range = {}
        for var_name in self.var_names:
            var_num_bits = self.var_enc_dict[var_name].num_bits
            self.var_bit_range[var_name] = (offset, offset + var_num_bits)
            offset += var_num_bits

        num_bits = offset
        super().__init__(num_bits)

    def encode(self, s):
        assert self.data_type.is_type_of(s)
        return tuple(flatten_to_list([self.var_enc_dict[var_name].encode(getattr(s, var_name))
                                      for var_name in self.var_names]))

    def encodes_var_form(self, vs, **kwargs):
        form = AND()
        for var_name, val in kwargs.items():
            start, stop = self.var_bit_range[var_name]
            form.add_args(self.var_enc_dict[var_name].encodes_form(vs[start:stop], val))
        return form

    def same_var_form(self, vs1, vs2, *args):
        if len(args) == 0:
            raise ValueError("No variable names for comparison.")
        form = AND()
        for var_name in args:
            start, stop = self.var_bit_range[var_name]
            form.add_args(equal_tuple_form(vs1[start:stop], vs2[start:stop]))
        return form

class ApplicationEncoding(Encoding):
    """
    Used to encode transition labels of symbolic automata
    In this case the explicit object is a function from a label encoding to a QBF over it
    This encoding relates an encoding and the explicit object (the function) by simply applying
    the function to the encoding.
    """
    def __init__(self, num_args, num_arg_bits):
        self.num_args = num_args
        self.num_arg_bits = num_arg_bits
        super().__init__(self.num_args * self.num_arg_bits)

    def encodes_form(self, vs, s):
        vs_split = [vs[i:i + self.num_arg_bits] for i in range(0, len(vs), self.num_arg_bits)]
        return s(*vs_split)


class BitVectorFunction:
    # used to map plant state encoding to label encoding
    def __init__(self, num_in_bits, num_out_bits, bit_forms):
        self.num_in_bits = num_in_bits
        self.num_out_bits = num_out_bits
        self.bit_forms = bit_forms

    def __call__(self, v_in):
        assert len(v_in) == self.num_in_bits
        v_out = self.bit_forms(v_in)
        assert len(v_out) == self.num_out_bits
        return v_out


class DefaultBitVectorFunction(BitVectorFunction):

    def __init__(self, in_enc, out_enc, explicit_func):
        """
        Create a symbolic function from an explicit function with given encodings
        for input and output domains

        Parameters
        ----------
        in_enc : SetEncoding
        out_enc : ConcreteEncoding
        explicit_func : callable
        """

        def sym_func(v_in):
            forms = [OR() for i in range(out_enc.num_bits)]
            for s in in_enc.vals:
                out_bits = out_enc.encode(explicit_func(s))
                for i in [i for i, bit in enumerate(out_bits) if bit]:
                    forms[i].add_args(in_enc.encodes_form(v_in, s))
            # TODO -> move simplification elsewhere to avoid always simplifying each call
            return [form.to_simplified() for form in forms]

        super().__init__(in_enc.num_bits, out_enc.num_bits, sym_func)


class ProductBitVectorFunction(BitVectorFunction):

    def __init__(self, *bv_funcs):
        in_bit_offset = [0]
        out_bit_offset = [0]
        for bvf in bv_funcs:
            in_bit_offset.append(in_bit_offset[-1] + bvf.num_in_bits)
            out_bit_offset.append(out_bit_offset[-1] + bvf.num_out_bits)

        def prod_func(v_in):
            return flatten_to_list([bvf(v_in[start:stop])
                                    for bvf, start, stop in zip(bv_funcs, in_bit_offset, in_bit_offset[1:])])
        super().__init__(in_bit_offset[-1], out_bit_offset[-1], prod_func)
