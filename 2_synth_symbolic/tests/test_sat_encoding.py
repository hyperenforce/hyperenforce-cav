"""
from hyper_synth.sat_encoding import ControllerSynthesisEncodingSAT
from tests.test_hyperauto import (hyper_auto_ex1, hyper_auto_ex2, plant_ex1,
                                  plant_ex2)


def _run_cont_synth(plant, h):
    enc = ControllerSynthesisEncodingSAT(plant, h)
    enc.encode()
    # Solve the SAT instance
    output = enc.solve()
    # Encode the result as a subautomaton of the plant
    controller = enc.decode_controller(output.model)
    return controller

def test_sat_encoding_tree():
    p1 = plant_ex1()
    p1 = p1.unfold_to_tree()
    h1 = hyper_auto_ex1()
    c1 = _run_cont_synth(p1, h1)
    assert c1
    assert c1.vcount() == 2
    assert c1.ecount() == 1

    p2 = plant_ex2()
    p2 = p2.unfold_to_tree()
    h2 = hyper_auto_ex2()
    c2 = _run_cont_synth(p2, h2)
    assert c2
    assert c2.vcount() == 5
    assert c2.ecount() == 4
"""
