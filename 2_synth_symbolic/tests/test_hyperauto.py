from hyper_synth.automata import Plant
from hyper_synth.datatype import DataType
from hyper_synth.encoding import (DataTypeEncoding, SetEncoding,
                                  equal_tuple_form)
from hyper_synth.hyperautomata import (ExplicitHyperAutomaton,
                                       SymbolicHyperAutomaton)
from hyper_synth.qbf import NOT, TRUE


def plant_ex1():
    """
    Tree with one root and two leaves outputting 'a' or 'b'
    """
    pt = DataType({"e": ["a", "b"]})
    plant = Plant(label_type=pt)
    # Add vertices to the plant labeled by their outputs
    plant.add_vertices(3, label=[pt.default_value, pt(e="a"), pt(e="b")])
    # Set initial state
    plant.initial_state_index = 0
    # Add edges labeled by whether they are controllable `"ec"` or uncontrollable `"eu"`
    plant.add_uncont_edge(0, 1)
    plant.add_cont_edge(0, 2)
    return plant


def hyper_auto_ex1():
    """
    For all runs. after initial state, output 'a'
    """
    # Plant output type
    pt = DataType({"e": ["a", "b"]})
    # Forall quantifier
    quants = (1, )
    h = ExplicitHyperAutomaton(quants, label_type=pt)
    h.add_vertices(3)
    h.initial_state_indices = [0]
    # All states of hyperautomaton are marked for now (safety)
    h.vs["marked"] = True
    # Hyperautomaton edges are labeled by pairs of outputs of the plant type
    h.add_edge(0, 1, (pt.default_value,))
    h.add_edge(1, 2, (pt(e="a"),))
    return h


def hyper_auto_ex1_existential():
    """
    There exists a path label "b"
    """
    # Plant output type
    pt = DataType({"e": ["a", "b"]})
    # Forall quantifier
    quants = (0, 1)
    h = ExplicitHyperAutomaton(quants, label_type=pt)
    h.add_vertices(3)
    h.initial_state_indices = [0]
    # All states of hyperautomaton are marked for now (safety)
    h.vs["marked"] = True
    # Hyperautomaton edges are labeled by pairs of outputs of the plant type
    h.add_edge(0, 1, (pt.default_value,))
    h.add_edge(1, 2, (pt(e="b"),))
    return h


def plant_ex2():
    """
    DAG with first transitions uncontrollable, and second transitions controllable to common terminal state
    """
    # Plant type with one output `u` representing the environment (uncontrollable)
    # and one output `c` that is designed (controllable)
    pt = DataType({"u": ["a", "b"], "c": ["c"]})
    plant = Plant(label_type=pt)
    # Add vertices to the plant labeled by their outputs
    plant.add_vertices(4, label=[pt(u="a", c="c"), pt(u="a", c="c"), pt(u="b", c="c"), pt(u="a", c="c")])
    # Set initial state
    plant.initial_state_index = 0
    # Add edges labeled by whether they are controllable `ec` or uncontrollable `euc`
    plant.add_uncont_edges([(0, 1), (0, 2)])
    plant.add_cont_edges([(1, 3), (2, 3)])
    return plant


def hyper_auto_ex2():
    """
    For all runs there exists another run with different outputs in the first step,
                                          and the same outputs in the second step
    """
    # Plant output type
    pt = DataType({"u": ["a", "b"], "c": ["c"]})
    # Quantifier for this hyperautomaton representing 1 universal quantifier followed by 1 existential quantifier
    quants = (1, 1)
    h = ExplicitHyperAutomaton(quants, label_type=pt)
    h.add_vertices(4)
    h.initial_state_indices = [0]
    # All states of hyperautomaton are marked for now (safety)
    h.vs["marked"] = True
    # Hyperautomaton edges are labeled by pairs of outputs of the plant type
    h.add_edges([(0, 1)], [(pt.default_value, pt.default_value)])
    h.add_edges([(1, 2), (1, 2)], [(pt(u="a", c="c"), pt(u="b", c="c")), (pt(u="b", c="c"), pt(u="a", c="c"))])
    h.add_edges([(2, 3)], [(pt(u="a", c="c"), pt(u="a", c="c"))])
    return h


def plant_ex1_no_type():
    """
    Tree with one root and two leaves outputting 'a' or 'b'
    """
    plant = Plant()
    # Add vertices to the plant labeled by their outputs
    plant.add_vertices(3, label=["a", "a", "b"])
    # Set initial state
    plant.initial_state_index = 0
    # Add edges labeled by whether they are controllable `"ec"` or uncontrollable `"eu"`
    plant.add_uncont_edge(0, 1)
    plant.add_cont_edge(0, 2)
    return plant


def hyper_auto_ex1_no_type():
    """
    For all runs. after initial state, output 'a'
    """
    # Forall quantifier
    quants = (1, )
    h = ExplicitHyperAutomaton(quants)
    h.add_vertices(3)
    h.initial_state_indices = [0]
    # All states of hyperautomaton are marked for now (safety)
    h.vs["marked"] = True
    # Hyperautomaton edges are labeled by pairs of outputs of the plant type
    h.add_edge(0, 1, ("a",))
    h.add_edge(1, 2, ("a",))
    return h


def test_unfold_to_tree():
    plant = plant_ex1()
    ptree = plant.unfold_to_tree()
    assert ptree.vcount() == 3
    assert ptree.ecount() == 2
    assert ptree.is_tree()

    plant = plant_ex2()
    ptree = plant.unfold_to_tree()
    assert ptree.vcount() == 5
    assert ptree.ecount() == 4
    assert ptree.is_tree()

    plant = plant_ex1_no_type()
    ptree = plant.unfold_to_tree()
    assert ptree.vcount() == 3
    assert ptree.ecount() == 2
    assert ptree.is_tree()


def test_self_compose():
    plant = plant_ex1()
    ps = plant.self_composition(1)
    assert ps.vcount() == 3
    assert ps.ecount() == 2

    plant = plant_ex2()
    ps = plant.self_composition(2)
    assert ps.vcount() == 6
    assert ps.ecount() == 8

    plant = plant_ex1_no_type()
    ps = plant.self_composition(1)
    assert ps.vcount() == 3
    assert ps.ecount() == 2


def test_auto_hyper_product():
    plant = plant_ex1()
    h = hyper_auto_ex1()
    ph = h.product_with_plant(plant)
    assert ph.vcount() == 2
    assert ph.ecount() == 1

    plant = plant_ex1()
    h = hyper_auto_ex1_existential()
    ph = h.product_with_plant(plant)
    assert ph.vcount() == 2
    assert ph.ecount() == 1

    plant = plant_ex2()
    h = hyper_auto_ex2()
    ph = h.product_with_plant(plant)
    assert ph.vcount() == 4
    assert ph.ecount() == 4

    plant = plant_ex1_no_type()
    h = hyper_auto_ex1_no_type()
    ph = h.product_with_plant(plant)
    assert ph.vcount() == 2
    assert ph.ecount() == 1

# Below are symbolic versions of the above hyperautomata

def symbolic_hyper_auto_ex1():
    """
    For all runs. after initial state, output 'a'
    """
    pt = DataType({"e": ["a", "b"]})
    pt_enc = DataTypeEncoding(pt)
    # Symbolic Hyperautomaton edges are labeled by functions mapping
    # plant state label encodings to a QBF over the encoding

    # This line requires `vpt` to exactly encode `pt(e="a")`
    #a_l = lambda vpt: pt_enc.encodes_form(vpt, pt(e="a"))
    # This line requires `vpt` to exactly encode a label with variable "e" set to value "a"
    a_l = lambda vpt: pt_enc.encodes_var_form(vpt, e="a")

    quants = (1, )
    h = SymbolicHyperAutomaton(quants, pt, pt_enc)
    h.add_vertices(3)
    h.initial_state_indices = [0]
    h.vs["marked"] = True
    h.add_edge(0, 1, a_l)
    h.add_edge(1, 2, a_l)
    return h, pt_enc


def symbolic_hyper_auto_ex2():
    """
    For all runs there exists another run with different outputs in the first step,
                                          and the same outputs in the second step
    """
    pt = DataType({"u": ["a", "b"], "c": ["c"]})
    pt_enc = DataTypeEncoding(pt)
    true_form = lambda v1, v2: TRUE
    #a_form = lambda v: pt_enc.encodes_var_form(v, u="a")
    #b_form = lambda v: pt_enc.encodes_var_form(v, u="b")
    #diff_form = lambda v1, v2: (a_form(v1) & b_form(v2)) | (a_form(v2) & b_form(v1))
    # equivalently
    diff_form = lambda v1, v2: NOT(equal_tuple_form(v1, v2))

    quants = (1, 1)
    h = SymbolicHyperAutomaton(quants, pt, pt_enc)
    h.add_vertices(4)
    h.initial_state_indices = [0]
    h.vs["marked"] = True
    h.add_edge(0, 1, true_form)
    h.add_edge(1, 2, diff_form)
    h.add_edge(2, 3, true_form)
    return h, pt_enc


def symbolic_hyper_auto_ex1_no_type():
    """
    For all runs. after initial state, output 'a'
    """
    label_type = None
    label_enc = SetEncoding(["a", "b"])
    a_form = lambda v: label_enc.encodes_form(v, "a")

    quants = (1,)
    h = SymbolicHyperAutomaton(quants, label_type, label_enc)
    h.add_vertices(3)
    h.initial_state_indices = [0]
    h.vs["marked"] = True
    h.add_edge(0, 1, a_form)
    h.add_edge(1, 2, a_form)
    return h, label_enc


def test_symbolic_hyper_auto():
    h, pt_enc = symbolic_hyper_auto_ex1()
    h, pt_enc = symbolic_hyper_auto_ex2()
    h, pt_enc = symbolic_hyper_auto_ex1_no_type()
