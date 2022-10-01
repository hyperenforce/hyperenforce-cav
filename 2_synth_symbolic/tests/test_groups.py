from hyper_synth.automata import Plant
from hyper_synth.datatype import DataType
from hyper_synth.encoding import (DataTypeEncoding, SetEncoding,
                                  equal_tuple_form)
from hyper_synth.hyperautomata import (ExplicitHyperAutomaton,
                                       SymbolicHyperAutomaton)
from hyper_synth.qbf import NOT, TRUE
from hyper_synth.qbf_encoding import ControllerSynthesisEncodingQBF


def plant_with_groups_ex1():
    pt = DataType({"e": ["a", "b"]})
    plant = Plant(label_type=pt)
    plant.add_vertices(3, label=[pt.default_value, pt(e="a"), pt(e="b")])
    plant.initial_state_index = 0
    # Add two controllable transitions with the same group
    # One is enabled if and only if the other is enabled
    plant.add_cont_edge(0, 1, group=1)
    plant.add_cont_edge(0, 2, group=1)
    return plant


def plant_with_groups_ex2():
    pt = DataType({"e": ["a", "b"]})
    plant = Plant(label_type=pt)
    plant.add_vertices(3, label=[pt.default_value, pt(e="a"), pt(e="b")])
    plant.initial_state_index = 0
    # Add two controllable transitions with opposite groups
    # One is enabled if and only if the other is not enabled
    plant.add_cont_edge(0, 1, group=1)
    plant.add_cont_edge(0, 2, group=-1)
    return plant


def hyper_auto_ex():
    # Create a hyperautomaton requiring all runs to be labeled "a"
    pt = DataType({"e": ["a", "b"]})
    pt_enc = DataTypeEncoding(pt)
    a_l = lambda vpt: pt_enc.encodes_var_form(vpt, e="a")
    true_l = lambda vpt: TRUE

    quants = (1, )
    h = SymbolicHyperAutomaton(quants, pt, pt_enc)
    h.add_vertices(3)
    h.initial_state_indices = [0]
    h.vs["marked"] = True
    h.add_edge(0, 1, true_l)
    h.add_edge(1, 2, a_l)
    return h, pt_enc


def _run_cont_synth(plant, h):
    prob = ControllerSynthesisEncodingQBF(plant, h, use_groups=True)
    prob.encode()
    output = prob.solve()
    if output.is_error:
        raise RuntimeError("Solver error: ", output.msg)
    return prob.decode_groups(output.model)


def test_groups():
    p1 = plant_with_groups_ex1()
    p2 = plant_with_groups_ex2()
    h, pt_enc = hyper_auto_ex()
    g1 = _run_cont_synth(p1, h)
    assert g1 is None

    g2 = _run_cont_synth(p2, h)
    assert set(g2) == {1}
