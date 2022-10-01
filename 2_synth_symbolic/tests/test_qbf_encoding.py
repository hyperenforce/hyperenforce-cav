from hyper_synth.qbf_encoding import ControllerSynthesisEncodingQBF
from tests.test_hyperauto import (hyper_auto_ex1, hyper_auto_ex1_existential,
                                  hyper_auto_ex1_no_type, hyper_auto_ex2,
                                  plant_ex1, plant_ex1_no_type, plant_ex2)


def _run_cont_synth(plant, h, unfold_tree=False, **kwargs):
    if unfold_tree:
        plant = plant.unfold_to_tree()
    prob = ControllerSynthesisEncodingQBF(plant, h, **kwargs)
    prob.encode()
    output = prob.solve()
    if output.is_error:
        raise RuntimeError("Solver error: ", output.msg)
    controller = prob.decode_controller(output.model)
    return controller


def check_examples(**kwargs):
    p1 = plant_ex1()
    h1 = hyper_auto_ex1()
    c1 = _run_cont_synth(p1, h1, **kwargs)
    assert c1
    assert c1.vcount() == 2
    assert c1.ecount() == 1

    pe = plant_ex1()
    he = hyper_auto_ex1_existential()
    ce = _run_cont_synth(pe, he, **kwargs)
    assert ce.vcount() == 3
    assert ce.ecount() == 2

    p2 = plant_ex2()
    h2 = hyper_auto_ex2()
    c2 = _run_cont_synth(p2, h2, **kwargs)
    assert c2
    if kwargs.get("unfold_tree", False):
        assert c2.vcount() == 5
    else:
        assert c2.vcount() == 4
    assert c2.ecount() == 4

    p3 = plant_ex1_no_type()
    h3 = hyper_auto_ex1_no_type()
    c3 = _run_cont_synth(p3, h3, **kwargs)
    assert c3
    assert c3.vcount() == 2
    assert c3.ecount() == 1


def test_qbf_encoding():
    check_examples()


def test_qbf_encoding_tree():
    check_examples(unfold_tree=True)


def test_qbf_encoding_no_step_quant():
    check_examples(quantify_path_steps=False)
