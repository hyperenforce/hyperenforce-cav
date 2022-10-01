import itertools

from hyper_synth.datatype import empty_type, empty_value
from hyper_synth.hyperautomata import ExplicitHyperAutomaton


# Expand constraints
def _expand_edges(edges, sub_type, super_type, n):
    return [(e[0], tuple(super_type.from_subvalues(t[i]) for i in range(n))) for e in edges
            for t in itertools.product(*[iter(sub_type.inverse_projection_gen(e[1][j])) for j in range(n)])]


def privacy_hyperautomaton(type_dict):
    """
    Construct a hyperautomaton encoding privacy/opacity for the obfuscation system.
    """
    quants = (1, 1)
    h = ExplicitHyperAutomaton(quants, label_type=type_dict["plant"])
    h.add_vertices(3)
    h.initial_state_indices = [0]
    h.vs["marked"] = True

    guess_val = type_dict["guess"](guess=1)
    no_guess_val = type_dict["guess"](guess=0)
    ng_type = type_dict["net"].product_type(type_dict["guess"])
    sg_type = type_dict["source_sec"].product_type(type_dict["guess"])

    edge_pairs = []
    e_ng = [((0, 0), (ng_type.from_subvalues(no_guess_val, obs),
                      ng_type.from_subvalues(gv, obs)))
            for obs in type_dict["net"]
            for gv in type_dict["guess"]]
    edge_pairs += _expand_edges(e_ng, ng_type, type_dict["plant"], 2)
    e_sg = [((0, 1), (sg_type.from_subvalues(guess_val, sec1),
                       sg_type.from_subvalues(gv, sec2)))
            for sec1 in type_dict["source_sec"]
            for sec2 in type_dict["source_sec"]
            for gv in type_dict["guess"]
            if sec1 != sec2]
    edge_pairs += _expand_edges(e_sg, sg_type, type_dict["plant"], 2)
    e_n = [((1, 2), (obs, obs))
           for obs in type_dict["net"]]
    edge_pairs += _expand_edges(e_n, type_dict["net"], type_dict["plant"], 2)
    e_all = [((2, 2), (empty_value, empty_value))]
    edge_pairs += _expand_edges(e_all, empty_type, type_dict["plant"], 2)

    edge_pairs = tuple(zip(*set(edge_pairs)))
    h.add_edges(edge_pairs[0], edge_pairs[1])

    return h

def pipeline_1_hyper_auto(type_dict, inputs, outputs):
    quants = (2,)
    h = ExplicitHyperAutomaton(quants, label_type=type_dict["plant"])
    h.add_vertices(4)
    h.initial_state_indices = [2]
    h.vs["marked"] = True


def pipeline_1_hyper_auto(type_dict):
    """
    Construct a hyperautomaton encoding the variable dependence in the first process of the obfuscation pipeline
    """
    quants = (2, )
    h = ExplicitHyperAutomaton(quants, label_type=type_dict["plant"])
    h.add_vertices(4)
    h.initial_state_indices = [2]
    h.vs["marked"] = True

    obs_key_type = type_dict["key"].product_type(type_dict["source_obs"])

    env_edges = []
    net_edges = []
    inf_edges = []

    # Env
    # If same observations and key, then must have same net outputs in next step
    env_edges += [((0, 1), (obs_key_val, obs_key_val)) for obs_key_val in obs_key_type]
    # Else no restrictions
    env_edges += [((0, 3), (obs_key_val1, obs_key_val2)) for obs_key_val1 in obs_key_type
                  for obs_key_val2 in obs_key_type if obs_key_val1 != obs_key_val2]
    env_edges += [((3, 3), (empty_value, empty_value))]

    # Net
    # Same net outputs
    net_edges += [((1, 2), (net_val, net_val)) for net_val in type_dict["net"]]
    # No restrictions
    net_edges += [((3, 3), (empty_value, empty_value))]

    # Inf
    # No restrictions
    inf_edges += [((2, 0), (empty_value, empty_value))]
    inf_edges += [((3, 3), (empty_value, empty_value))]

    edge_pairs = []
    edge_pairs += _expand_edges(env_edges, type_dict["env"], type_dict["plant"], 2)
    edge_pairs += _expand_edges(net_edges, type_dict["net"], type_dict["plant"], 2)
    edge_pairs += _expand_edges(inf_edges, type_dict["inf"], type_dict["plant"], 2)

    edge_pairs = tuple(zip(*set(edge_pairs)))
    h.add_edges(edge_pairs[0], edge_pairs[1])

    return h


def pipeline_2_hyper_auto(type_dict):
    """
    Construct a hyperautomaton encoding the variable dependence in the second process of the obfuscation pipeline
    """
    quants = (2, )
    h = ExplicitHyperAutomaton(quants, label_type=type_dict["plant"])
    h.add_vertices(4)
    h.initial_state_indices = [1]
    h.vs["marked"] = True

    env_edges = []
    net_edges = []
    inf_edges = []

    # Net
    # If same outputs, then must have same inf outputs in next step
    net_edges += [((0, 1), (net_val, net_val)) for net_val in type_dict["net"]]
    # Else no restrictions
    net_edges += [((0, 3), (net_val1, net_val2)) for net_val1 in type_dict["net"]
                  for net_val2 in type_dict["net"] if net_val1 != net_val2]
    net_edges += [((3, 3), (empty_value, empty_value))]

    # Inf
    # Same inf outputs
    inf_edges += [((1, 2), (inf_val, inf_val)) for inf_val in type_dict["inf"]]
    # No restrictions
    inf_edges += [((3, 3), (empty_value, empty_value))]

    # Env
    # If same key
    env_edges += [((2, 0), (key_val, key_val)) for key_val in type_dict["key"]]
    # If different key
    env_edges += [((2, 3), (key_val1, key_val2)) for key_val1 in type_dict["key"]
                  for key_val2 in type_dict["key"] if key_val1 != key_val2]
    # No restriction
    env_edges += [((3, 3), (empty_value, empty_value))]

    edge_pairs = []
    edge_pairs += _expand_edges(env_edges, type_dict["env"], type_dict["plant"], 2)
    edge_pairs += _expand_edges(net_edges, type_dict["net"], type_dict["plant"], 2)
    edge_pairs += _expand_edges(inf_edges, type_dict["inf"], type_dict["plant"], 2)

    edge_pairs = tuple(zip(*set(edge_pairs)))
    h.add_edges(edge_pairs[0], edge_pairs[1])

    return h


def lin_hyper_auto(type_dict, inf_names):
    """
    Construct a hyperautomaton encoding the linear spec for obfuscation (i.e. correct inferences)
    Note this can be viewed as just a normal automaton.
    """
    source_vals = list(iter(type_dict["source"]))
    source_index = {source_val: i+2 for i, source_val in enumerate(source_vals)}
    net_index = {source_val: i+2+len(source_vals) for i, source_val in enumerate(source_vals)}
    inf_map = {source_val: type_dict["inf"](**{inf_names[k]: v for k, v in source_val._asdict().items()})
               for source_val in source_vals}

    quants = (1, )
    h = ExplicitHyperAutomaton(quants, label_type=type_dict["plant"])
    h.add_vertices(2 + 2 * len(source_vals))
    h.initial_state_indices = [0]
    h.vs["marked"] = True
    env_edges = []
    net_edges = []
    inf_edges = []

    # Env
    # Store source output
    env_edges += [((0, 1), (type_dict["env"].default_value,))]
    env_edges += [((1, source_index[source_val]), (source_val,)) for source_val in source_vals]

    # Net
    # Remember source output
    net_edges += [((source_index[source_val], net_index[source_val]), (net_val1,))
                  for net_val1 in type_dict["net"] for source_val in source_vals]
    # Inf
    # Inf output must match source
    inf_edges += [((net_index[source_val], 1), (inf_map[source_val],)) for source_val in source_vals]

    edge_pairs = []
    edge_pairs += _expand_edges(env_edges, type_dict["env"], type_dict["plant"], 1)
    edge_pairs += _expand_edges(net_edges, type_dict["net"], type_dict["plant"], 1)
    edge_pairs += _expand_edges(inf_edges, type_dict["inf"], type_dict["plant"], 1)
    edge_pairs = tuple(zip(*set(edge_pairs)))
    h.add_edges(edge_pairs[0], edge_pairs[1])
    return h
