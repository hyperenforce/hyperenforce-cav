import itertools
import math


def flatten_to_list(vals):
    return list(itertools.chain.from_iterable(vals))


def to_binary(val, num_bits):
    """
    Convert a decimal value to its binary representation

    Parameters
    ----------
    val : int
        The decimal value to convert
    num_bits : int
        The number of bits in the output (result is left padded with zeros)

    Returns
    -------
    tuple[bool]
    """
    assert val < 2 ** num_bits
    if num_bits == 0:
        return ()
    return tuple((v == '1' for v in f"{val:0{num_bits}b}"))


class SetEncoding:
    """
    A Boolean encoding of a set of values

    Attributes
    -------
    vals : list
        The encoded values
    num_bits : int
        The number of bits used
    bits : list[int]
        The name of each bit
    to_bits : dict[obj, tuple[bool]]
        Mapping from value to encoding as bit tuple
    from_bits : dict[tuple[bool], bits]
        Mapping from bit tuple to decoded value
    """

    def __init__(self, vals):
        """
        Construct a Boolean encoding of a set of values.

        Parameters
        ----------
        vals : iterable
            The values to encode
        """
        self.vals = list(set(vals))
        self.num_bits = math.ceil(math.log2(len(self.vals)))
        self.bits = list(range(self.num_bits))
        self.to_bits = {val: to_binary(val, self.num_bits) for val in self.vals}
        self.from_bits = {to_binary(val, self.num_bits): val for val in self.vals}

    def __str__(self):
        return f"Encoding of {self.vals}: \n{self.to_bits}\n"
