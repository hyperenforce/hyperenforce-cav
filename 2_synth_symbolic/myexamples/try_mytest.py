import os
from hyper_synth.automata import HyperAutomaton, Plant
from hyper_synth.datatype import DataType
from hyper_synth.qbf_encoding import ControllerSynthesisEncodingQBF
from tests.test_hyperauto import (hyper_auto_ex1, hyper_auto_ex1_no_type,
                                  hyper_auto_ex2, plant_ex1, plant_ex1_no_type,
                                  plant_ex2)

def my_model():
    pt = DataType({'controllable': ['0', 'null'], 'PC': ['5', 'null'], 'ucon_x': ['true', 'false', 'null'], 'con_y': ['true', 'false', 'null']})
    plant = Plant(label_type=pt)
    # add an empty init state
    plant.add_vertex(label=pt(controllable='null', PC='null', ucon_x='null', con_y='null')) # index:0
    # trace 1
    plant.add_vertex(label=pt(controllable='0', PC='5', ucon_x='true', con_y='true')) # index:1
    plant.add_vertex(label=pt(controllable='0', PC='12', ucon_x='true', con_y='true')) # index:2
    plant.add_vertex(label=pt(controllable='0', PC='16', ucon_x='true', con_y='true')) # index:3

    plant.initial_state_index = 0

    plant.add_uncont_edge(0, 1)
    plant.add_uncont_edge(1, 2)
    plant.add_uncont_edge(2, 3)

    return plant

'''
A hyper
'''
def my_h():
    # Plant output type
    pt = DataType({'controllable': ['0', 'null'], 'PC': ['5', 'null'], 'ucon_x': ['true', 'false', 'null'], 'con_y': ['true', 'false', 'null']})
    # Forall quantifier
    quants = (1, )
    h = HyperAutomaton(quants, label_type=pt)
    h.add_vertices(3, )
    h.initial_state_indices = [0]
    h.add_edge(0, 1, (pt(controllable='null', PC='null', ucon_x='null', con_y='null'),))
    h.add_edge(1, 2, (pt(controllable='0'),))
    return h

def _run_cont_synth(plant, h):
    prob = ControllerSynthesisEncodingQBF(plant, h, do_optimization=False)
    prob.encode()
    output = prob.solve()
    if output.is_error:
        raise RuntimeError('Solver error: ', output.msg)
    controller = prob.decode_controller(output.model)
    return controller


p1 = my_model()
h1 = my_h()


# p1 = plant_ex1()
# h1 = hyper_auto_ex1()
c1 = _run_cont_synth(p1, h1)
print(c1)
print(type(c1))
print(c1.vs['label'])
