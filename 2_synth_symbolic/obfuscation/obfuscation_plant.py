import warnings

from hyper_synth.automata import Plant
from hyper_synth.datatype import DataType
from hyper_synth.encoding import (BitVectorFunction, ConcreteEncoding,
                                  DataTypeEncoding, ProductBitVectorFunction,
                                  SetEncoding)
from hyper_synth.util import flatten_to_list


def construct_guess_plant():
    """
    Construct an automaton modeling the "guess" behavior.
    The "guess" value can only be true at one point in time.
    This is useful for specifying opacity in HyperLTL
    """
    guess_type = DataType({"guess": [0, 1]})
    guess = Plant(label_type=guess_type, name_type=guess_type)
    guess.add_vertices(3, label=[guess_type(guess=i) for i in [0, 1, 0]])
    guess.vs["name"] = guess.vs["label"]
    guess.add_edges([(0, 0), (0, 1), (1, 2), (2, 2)], [Plant.euc] * 4)
    guess.initial_state_index = 0
    return guess


def construct_key_plant(num_keys=2):
    """
    Construct an automaton modeling the selection of one of the given number of keys.
    The "key" is selected in the first step and remains constant thereafter.

    Parameters
    ----------
    num_keys : int
        The number of keys

    Returns
    -------
    Plant
        The plant modeling the key behavior

    """
    key_type = DataType({"key": list(range(num_keys))})
    key = Plant(label_type=key_type, name_type=key_type)
    key.add_vertices(num_keys+1, label=([key_type.default_value] + [key_type(key=i) for i in range(num_keys)]))
    key.vs["name"] = key.vs["label"]
    key.add_edges([(0, i+1) for i in range(num_keys)], [Plant.euc] * num_keys)
    key.add_edges([(i+1, i+1) for i in range(num_keys)], [Plant.euc] * num_keys)
    key.initial_state_index = 0
    return key


def construct_universal_plant(label_type, controllable=True, initial_val=None):
    """
    Construct a plant representing all output sequences over the given type with transitions labeled
    as either controllable or uncontrollable according to the input.

    Parameters
    ----------
    label_type : DataType
        The output type of the plant
    controllable :
        If True, then all transitions are labeled as controllable. Otherwise uncontrollable

    Returns
    -------
    Plant
       The plant
    """
    if initial_val is None:
        initial_val = label_type.default_value

    plant = Plant(label_type=label_type, name_type=label_type)
    values = [v for v in label_type]
    num_values = label_type.num_values()
    plant.add_vertices(num_values, label=values)
    plant.vs["name"] = plant.vs["label"]
    plant.initial_state_index = values.index(initial_val)
    event = Plant.ec if controllable else Plant.euc
    plant.add_edges([(i, j) for i in range(num_values) for j in range(num_values)], [event] * (num_values * num_values))
    return plant


def construct_universal_network(source, obs_out, net_names):
    """
    Construct a plant modeling all possible outputs on the network.

    Parameters
    ----------
    source : Plant
    obs_out : set[str]
        The names of variables in the source type that can be observed nominally
    net_names : dict[str, str]
        A mapping from variable names in the source type to new variable names in the network type.

    Returns
    -------
    network : Plant
        The plant modeling the universal network
    """
    net_type = source.label_type.subtype(obs_out).copy_with_new_names(net_names)
    init_net = net_type(**{net_names[k]: v for k, v in source.initial_state["label"]._asdict().items()
                           if k in obs_out})
    net = construct_universal_plant(net_type, initial_val=init_net)
    return net


def construct_universal_inference(source, inf_out, inf_names):
    """
    Construct a plant modeling all possible outputs for inference.

    Parameters
    ----------
    source : Plant
    inf_out : list[str]
        The names of variables in the source type to be inferred
    inf_names : dict[str, str]
        A mapping from variable names in the source type to new variable names in the inference type.

    Returns
    -------
    inf : Plant
        The plant modeling universal inference
    """
    inf_type = source.label_type.subtype(inf_out).copy_with_new_names(inf_names)
    init_inf = inf_type(**{inf_names[k]: v for k, v in source.initial_state["label"]._asdict().items()
                           if k in inf_out})
    inf = construct_universal_plant(inf_type, initial_val=init_inf)
    return inf


def construct_source_network(source, obs_out, net_names):
    """
    Construct a plant modeling all outputs on the network that mimic the source.

    Parameters
    ----------
    source : Plant
    obs_out : list[str]
    net_names : dict[str, str]

    Returns
    -------
    network : Plant
        The plant modeling the network
    """
    net_type = source.label_type.subtype(obs_out).copy_with_new_names(net_names)
    name_type = source.name_type.copy_with_new_names(net_names)
    net = Plant(label_type=net_type, name_type=name_type)
    net.add_vertices(source.vcount(), init=source.vs["init"],
                     label=[net_type(**{net_names[k]: v for k, v in vl._asdict().items() if k in obs_out})
                            for vl in source.vs["label"]],
                     name=[name_type(**{net_names[k]: v for k, v in vn._asdict().items()})
                           for vn in source.vs["name"]])
    net.add_cont_edges([(e.source, e.target) for e in source.es])
    return net


def create_obfuscation_plant_and_spec(source, sec_out, inf_out, obs_out,
                                      net_names=None, inf_names=None,
                                      num_keys=2, remove_bad_inf=True,
                                      remove_bad_obf=True, use_name_type=True,
                                      cs_opacity=True, source_as_inf=False):
    """
    Create the arena for the controller synthesis problem for privacy enforcement problem.
    Events alternate between turns for the plant (uncontrollable) and the network and inference (controllable).
    The plant moves first.


    Parameters
    ----------
    source : Plant
        The model of the source
    sec_out : set[str]
        The names of variables in the source type to be kept secret
    inf_out : set[str]
        The names of variables in the source type that should be inferred
    obs_out : set[str]
        The names of variables in the source type that can be observed nominally
    net_names : dict[str, str]
        A mapping from variable names in the source type to new variable names in the network type.
    inf_names : dict[str, str]
        A mapping from variable names in the source type to new variable names in the inference type.
    num_keys : int

    Returns
    -------
    plant : Plant
        The model of the plant
    type_dict : dict[str,DataType]
        The types of the plant outputs
    spec_dict : dict[str,list[str]]
        The different kinds of specifications for the system
        "linear": A list of forall HyperLTL specifications (i.e., LTL)
        "pipe": A list of forall.forall HyperLTL specifications corresponding to the pipeline synthesis problem
        "privacy": A list of forall.exists HyperLTL specifications expressing opacity to an observer that knows about obfuscation
    plant_state_encoding
    label_encoding
    label_func
    """
    if not use_name_type:
        raise NotImplementedError()

    if source.name_type is None:
        index_type = DataType({"source_index": source.vs.indices})
        source.name_type = index_type.product_type(source.label_type)
        source.vs["name"] = [source.name_type.from_subvalues(index_type(source_index=v.index),
                                                             v["label"]) for v in source.vs]

    added_automata = []
    if cs_opacity:
        guess = construct_guess_plant()
        added_automata.append(guess)
    key = construct_key_plant(num_keys=num_keys)
    added_automata.append(key)

    env = source.sync_compose(*added_automata)

    if net_names is None:
        net_names = {n: f"net_{n}" for n in obs_out}
    if remove_bad_obf:
        net = construct_source_network(source, obs_out, net_names)
    else:
        net = construct_universal_network(source, obs_out, net_names)

    if source_as_inf:
        if inf_names is None:
            warnings.warn("Ignoring `inf_names` as the inference component is being modeled by the source")
        remove_bad_inf = False
        inf_names = {n: n for n in inf_out}
        inf_type = source.label_type.subtype(inf_out)
        net_inf = net
    else:
        if inf_names is None:
            inf_names = {n: f"inf_{n}" for n in inf_out}
        inf = construct_universal_inference(source, inf_out, inf_names)
        inf_type = inf.label_type
        net_inf = net.sync_compose(inf)

    plant = env.alternating_compose(net_inf)

    if remove_bad_inf:
        remove_bad_inf_states(source, inf_names, plant)

    # todo - make sure type encodings coincide
    plant_state_name_encoding = DataTypeEncoding(plant.name_type)
    plant_state_encoding = plant_state_name_encoding
    label_encoding = DataTypeEncoding(plant.label_type)
    assert plant.label_type.is_subtype(plant.name_type)
    funcs = []
    for var_name in plant.name_type.var_names():
        num_in_bits = plant_state_name_encoding.var_enc_dict[var_name].num_bits
        if var_name in plant.label_type.var_names():
            num_out_bits = label_encoding.var_enc_dict[var_name].num_bits
            func = lambda v: v
        else:
            num_out_bits = 0
            func = lambda v: ()
        funcs.append(BitVectorFunction(num_in_bits, num_out_bits, func))
    label_func = ProductBitVectorFunction(*funcs)

    type_dict = {"plant": plant.label_type,
                 "env": env.label_type,
                 "key": key.label_type,
                 "source": source.label_type,
                 "source_obs": source.label_type.subtype(obs_out),
                 "source_sec": source.label_type.subtype(sec_out),
                 "source_inf": source.label_type.subtype(inf_out),
                 "net": net.label_type,
                 "inf": inf_type}

    if cs_opacity:
        type_dict["guess"] = guess.label_type

    lin_specs = [
        "forall pi1. " + (" & ".join([f"G ({v_inf}[pi1] = X X {inf_names[v_inf]}[pi1])" for v_inf in inf_out]))
    ]

    def same_vals(var_names):
        return "(" + (" & ".join([f"{vn}[pi1] = {vn}[pi2]" for vn in var_names])) + ")"

    def same_out_until_in(v_out, v_in):
        return f"({same_vals(v_out)} W !{same_vals(v_in)})"

    def key_dependence(v_out, v_in):
        return f"forall pi1. forall pi2. {same_vals(['key'])} | {same_out_until_in(v_out, v_in)}"

    """
    pipe_specs = [
        key_dependence(net.label_type.var_names(), obs_out),
        key_dependence(inf.label_type.var_names(), net.label_type.var_names()),
    ]

    # privacy spec
    priv_specs = []
    for v_sec in sec_out:
        spec = f"forall pi1. exists pi2. (guess[pi1] R (X {same_vals(net.label_type.var_names())})) & " \
               f"G (guess[pi1] -> !{same_vals([v_sec])})"
        priv_specs.append(spec)

    spec_dict = {"linear": lin_specs,
                 "pipe": pipe_specs,
                 "privacy": priv_specs}
    """

    return plant, type_dict, None, plant_state_encoding, label_encoding, label_func


def remove_bad_inf_states(source, inf_names, plant):
    bad_indices = []
    for v in plant.vs:
        source_vars = source.label_type.var_names()
        if any(getattr(v["label"], var_name) != getattr(v["label"], inf_names[var_name]) and
               v["name"].async_counter == 0
               for var_name in source_vars):
            bad_indices.append(v.index)
    plant.delete_vertices(plant.vs.select(bad_indices))
