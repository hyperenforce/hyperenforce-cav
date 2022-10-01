from hyper_synth.automata import Plant
from hyper_synth.hyperautomata import ExplicitHyperAutomaton
from hyper_synth.qbf_encoding import ControllerSynthesisEncodingQBF


def _run_cont_synth(plant, h):
    prob = ControllerSynthesisEncodingQBF(plant, h, do_optimization=True)
    prob.encode()
    output = prob.solve()
    if output.is_error:
        raise RuntimeError("Solver error: ", output.msg)
    controller = prob.decode_controller(output.model)
    return controller


def plant_opt():
    """
    Tree with three leaves outputting 'b', 'c', or 'd'
    """
    plant = Plant()
    plant.add_vertices(4, label=['a', 'b', 'c', 'd'])
    plant.initial_state_index = 0
    # specify cost to remove edge with "weight" attribute
    plant.add_cont_edges([(0, 1), (0, 2), (0, 3)], weight=[1, 2, 3])
    return plant


def hyper_auto_opt1():
    """
    Controller must have two distinct paths
    """
    # Forall Exists quantifier
    quants = (1, 1)
    h = ExplicitHyperAutomaton(quants)
    h.add_vertices(3)
    h.initial_state_indices = [0]
    h.vs["marked"] = True

    h.add_edges([(0, 1)], [('a', 'a')])
    labels = ['b', 'c', 'd']
    h.add_edges([(1, 2)] * 6, [(l1, l2) for l1 in labels for l2 in labels if l1 != l2])
    return h


def hyper_auto_opt2():
    """
    Controller must have at most two distinct paths
    """
    # Forall^3 quantifier
    quants = (3,)
    h = ExplicitHyperAutomaton(quants)
    h.add_vertices(3)
    h.initial_state_indices = [0]
    h.vs["marked"] = True

    h.add_edges([(0, 1)], [('a', 'a', 'a')])
    labels = ['b', 'c', 'd']
    h.add_edges([(1, 2)] * (3 * 3 * 3 - 3 * 2),
                [(l1, l2, l3) for l1 in labels for l2 in labels for l3 in labels if len({l1, l2, l3}) != 3])
    return h


def test_qbf_encoding_opt():
    p1 = plant_opt()
    h1 = hyper_auto_opt1()
    c1 = _run_cont_synth(p1, h1)
    # Optimal controller should keep all paths
    assert c1
    assert c1.vcount() == 4
    assert c1.ecount() == 3

    p2 = plant_opt()
    h2 = hyper_auto_opt2()
    c2 = _run_cont_synth(p2, h2)
    # Optimal controller must remove lowest cost path (to state 1)
    assert c2
    assert c2.vcount() == 3
    assert c2.ecount() == 2
    assert 1 not in c2.vs["name"]
