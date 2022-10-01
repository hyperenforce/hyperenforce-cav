from hyper_synth.qbf_encoding import ControllerSynthesisEncodingQBF
from tests.test_hyperauto import (hyper_auto_ex1, hyper_auto_ex1_no_type,
                                  hyper_auto_ex2, plant_ex1, plant_ex1_no_type,
                                  plant_ex2)


def _run_cont_synth(plant, h, **kwargs):
    # Encode the synthesis problem as an instance of QBF satisfaction
    prob = ControllerSynthesisEncodingQBF(plant, h, **kwargs)
    prob.encode()
    # Solve the QBF instance
    output = prob.solve()
    if output.is_error:
        raise RuntimeError("Solver error: ", output.msg)
    # Encode the solution as a subautomaton of the plant
    controller = prob.decode_controller(output.model)
    return controller


def test_qbf_encoding():
    p1 = plant_ex1()
    h1 = hyper_auto_ex1()
    c1 = _run_cont_synth(p1, h1)
    assert c1
    assert c1.vcount() == 2
    assert c1.ecount() == 1

    p2 = plant_ex2()
    h2 = hyper_auto_ex2()
    c2 = _run_cont_synth(p2, h2)
    assert c2
    assert c2.vcount() == 4
    assert c2.ecount() == 4

    p3 = plant_ex1_no_type()
    h3 = hyper_auto_ex1_no_type()
    c3 = _run_cont_synth(p3, h3)
    assert c3
    assert c3.vcount() == 2
    assert c3.ecount() == 1


def test_qbf_encoding_tree():
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


def test_qbf_encoding_minmimization():
    p1 = plant_ex1()
    h1 = hyper_auto_ex1()
    c1 = _run_cont_synth(p1, h1, use_minimization=True)
    assert c1
    assert c1.vcount() == 2
    assert c1.ecount() == 1

    p2 = plant_ex2()
    h2 = hyper_auto_ex2()
    c2 = _run_cont_synth(p2, h2, use_minimization=True)
    assert c2
    assert c2.vcount() == 4
    assert c2.ecount() == 4


def test_qbf_encoding_no_step_quant():
    p1 = plant_ex1()
    h1 = hyper_auto_ex1()
    c1 = _run_cont_synth(p1, h1, quantify_path_steps=False)
    assert c1
    assert c1.vcount() == 2
    assert c1.ecount() == 1

    p2 = plant_ex2()
    h2 = hyper_auto_ex2()
    c2 = _run_cont_synth(p2, h2, quantify_path_steps=False)
    assert c2
    assert c2.vcount() == 4
    assert c2.ecount() == 4
