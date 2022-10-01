
from hyper_synth.datatype import empty_value
from hyper_synth.encoding import DataTypeEncoding
from hyper_synth.hyperautomata import SymbolicHyperAutomaton
from hyper_synth.qbf import AND, IMPLIES, NOT, TRUE, flatten_to_list


def _negate_l(l_map):
    return lambda *v: NOT(l_map(*v)).to_simplified()

def _and_l(l_map1, l_map2):
    return lambda *v: AND(l_map1(*v), l_map2(*v)).to_simplified()

def _true_l():
    return lambda *v: TRUE

def _implication_l(l_map1, l_map2):
    return lambda *v: IMPLIES(l_map1(*v), l_map2(*v)).to_simplified()

def _guess_l(pt_enc, type_dict):
    return lambda v1, v2: pt_enc.encodes_var_form(v1, guess=1).to_simplified()

def _same_l(pt_enc, type_dict, *args):
    return lambda v1, v2: pt_enc.same_var_form(v1, v2, *flatten_to_list(
        [type_dict[arg].var_names() for arg in args])).to_simplified()

def _encodes_l(pt_enc, type_dict, **kwargs):
    val_dict = dict()
    for k, v in kwargs.items():
        for var_name in type_dict[k].var_names():
            val_dict[var_name] = getattr(v, var_name)
    return lambda v1: pt_enc.encodes_var_form(v1, **val_dict).to_simplified()

def privacy_sybmolic_hyperautomaton(type_dict, pt_enc, cs_opacity=True):
    """
    Construct a hyperautomaton encoding privacy/opacity for the obfuscation system.
    """
    pt = type_dict["plant"]

    quants = (1, 1)
    h = SymbolicHyperAutomaton(quants, label_type=pt, label_encoding=pt_enc)

    sec_var = next(iter(type_dict["source_sec"].var_names()))
    sec_l = lambda v1, v2: pt_enc.encodes_var_form(v2, **{sec_var:(True,)})

    #sec_l = _same_l(pt_enc, type_dict, "source_sec")

    if cs_opacity:


        h.add_vertices(8)
        h.initial_state_indices = [0]
        h.vs["marked"] = True

        h.add_edge(0, 1, _true_l())

        h.add_edge(1, 2, _true_l())
        h.add_edge(1, 5, _guess_l(pt_enc, type_dict))

        h.add_edge(2, 3, _same_l(pt_enc, type_dict, "net"))

        h.add_edge(3, 2, _negate_l(_guess_l(pt_enc, type_dict)))
        h.add_edge(3, 4, _and_l(_guess_l(pt_enc, type_dict), _negate_l(sec_l)))
        h.add_edge(3, 6, _true_l())

        h.add_edge(4, 5, _same_l(pt_enc, type_dict, "net"))
        h.add_edge(5, 5, _true_l())

        h.add_edge(6, 7, _true_l())

        """
        h.add_edge(0, 1, _true_l())
        h.add_edge(1, 1, _and_l(_negate_l(_guess_l(pt_enc, type_dict)), _same_l(pt_enc, type_dict, "net")))
        h.add_edge(1, 2, _and_l(_guess_l(pt_enc, type_dict), _negate_l(_same_l(pt_enc, type_dict, "source_sec"))))
        h.add_edge(2, 3, _same_l(pt_enc, type_dict, "net"))
        h.add_edge(3, 3, _true_l())
        """
    else:
        h.add_vertices(2)
        h.initial_state_indices = [0]
        h.vs["marked"] = True

        h.add_edge(0, 1, _true_l())
        h.add_edge(1, 1, _and_l(_negate_l(sec_l), _same_l(pt_enc, type_dict, "net")))

    return h


def dependency_sybmolic_hyper_auto(type_dict, pt_enc, inputs, outputs, alternate):
    pt = type_dict["plant"]

    quants = (2,)
    h = SymbolicHyperAutomaton(quants, label_type=pt, label_encoding=pt_enc)
    if alternate:
        h.add_vertices(3)
        h.initial_state_indices = [1]
        h.vs["marked"] = True

        h.add_edge(0, 1, _true_l())
        h.add_edge(1, 0, _same_l(pt_enc, type_dict, *outputs))
        h.add_edge(1, 2, _negate_l(_same_l(pt_enc, type_dict, *inputs)))
        h.add_edge(2, 2, _true_l())
    else:
        h.add_vertices(2)
        h.initial_state_indices = [0]
        h.vs["marked"] = True

        h.add_edge(0, 0, _same_l(pt_enc, type_dict, *outputs))
        h.add_edge(0, 1, _negate_l(_same_l(pt_enc, type_dict, *inputs)))
        h.add_edge(1, 1, _true_l())
    return h

def pipeline_1_sybmolic_hyper_auto(type_dict, pt_enc):
    """
    Construct a hyperautomaton encoding the variable dependence in the first process of the obfuscation pipeline
    """
    return dependency_sybmolic_hyper_auto(type_dict, pt_enc,
                                          inputs=["key", "source"], outputs=["net"],
                                          alternate=False)


def pipeline_2_sybmolic_hyper_auto(type_dict, pt_enc, alternate=False):
    """
    Construct a hyperautomaton encoding the variable dependence in the second process of the obfuscation pipeline
    """
    return dependency_sybmolic_hyper_auto(type_dict, pt_enc,
                                          inputs=["key", "net"], outputs=["inf"],
                                          alternate=alternate)


def lin_symbolic_hyper_auto(type_dict, inf_names, pt_enc):
    """
    Construct a hyperautomaton encoding the linear spec for obfuscation (i.e. correct inferences)
    Note this can be viewed as just a normal automaton.
    """
    source_vals = list(iter(type_dict["source"]))
    # map from source value to state index for source turn
    source_index = {source_val: i + 2 for i, source_val in enumerate(source_vals)}
    # map from source value to state index for net turn
    net_index = {source_val: i + 2 + len(source_vals) for i, source_val in enumerate(source_vals)}
    # map from source value to matching inference value
    inf_map = {source_val: type_dict["inf"](**{inf_names[k]: v for k, v in source_val._asdict().items()})
               for source_val in source_vals}

    pt = type_dict["plant"]

    quants = (1,)
    h = SymbolicHyperAutomaton(quants, label_type=pt, label_encoding=pt_enc)

    h.add_vertices(2 + 2 * len(source_vals))
    h.initial_state_indices = [0]
    h.vs["marked"] = True

    edge_pairs = []
    # Env
    # Store source output
    edge_pairs += [((0, 1), _true_l())]
    edge_pairs += [((1, source_index[source_val]), _encodes_l(pt_enc, type_dict, source=source_val))
                   for source_val in source_vals]

    # Net
    # Remember source output
    edge_pairs += [((source_index[source_val], net_index[source_val]),
                    _encodes_l(pt_enc, type_dict, source=source_val))
                   for source_val in source_vals]
    edge_pairs += [((source_index[source_val], net_index[source_val]), _true_l())
                   for source_val in source_vals]
    # Inf
    # Inf output must match source
    edge_pairs += [((net_index[source_val], 1), _encodes_l(pt_enc, type_dict, inf=inf_map[source_val]))
                   for source_val in source_vals]

    edge_pairs = tuple(zip(*set(edge_pairs)))
    h.add_edges(edge_pairs[0], edge_pairs[1])
    return h
