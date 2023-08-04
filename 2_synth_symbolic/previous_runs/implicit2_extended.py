import os
from hyper_synth.automata import HyperAutomaton, Plant
from hyper_synth.datatype import DataType
from hyper_synth.qbf_encoding import ControllerSynthesisEncodingQBF
from tests.test_hyperauto import (hyper_auto_ex1, hyper_auto_ex1_no_type,
                                  hyper_auto_ex2, plant_ex1, plant_ex1_no_type,
                                  plant_ex2)
pt = DataType({'is_cont': [0, 'null'], 'PC': [5, 'null'], 'con_y': ['true', 'false', 'null']})
plant = Plant(label_type=pt)
# add an empty init state
plant.add_vertex(label=pt.default_value)
# make it initial state
plant.initial_state_index = 0

# trace 1
# ucon_x = true
# ucon_z = true
# supp_0 = true
plant.add_vertex(label=pt(is_cont="0", PC="5", con_y="true")) # index:1
plant.add_uncont_edges([(0, 1)], weight=[1])
plant.add_vertex(label=pt(is_cont="0", PC="13", con_y="true")) # index:2
plant.add_uncont_edges([(1, 2)], weight=[1])
plant.add_vertex(label=pt(is_cont="0", PC="16", con_y="true")) # index:3
plant.add_uncont_edges([(2, 3)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="25", con_y="true")) # index:4
plant.add_cont_edges([(3, 4)], weight=[1])

# trace 2
# ucon_x = false
# ucon_z = false
# supp_0 = false
plant.add_vertex(label=pt(is_cont="0", PC="5", con_y="false")) # index:5
plant.add_uncont_edges([(0, 5)], weight=[1])
plant.add_vertex(label=pt(is_cont="0", PC="13", con_y="false")) # index:6
# repeating uncontrollable edge: (5,5), ignore 
plant.add_vertex(label=pt(is_cont="0", PC="16", con_y="false")) # index:7
plant.add_uncont_edges([(5, 7)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="25", con_y="false")) # index:8
plant.add_cont_edges([(7, 8)], weight=[1])

# trace 3
# ucon_x = false
# ucon_z = true
# supp_0 = false
# repeating state at PC=5, goes back to index:5
# repeating uncontrollable edge: (0,5), ignore 
# repeating state at PC=13, goes back to index:6
plant.add_uncont_edges([(5, 6)], weight=[1])
# repeating state at PC=25, goes back to index:7
plant.add_uncont_edges([(6, 7)], weight=[1])
# repeating state at PC=25, goes back to index:8
# repeating controllable edge: (7,8), ignore 
#
#
#
"""
A hyper automaton
"""
# Plant output type
# Forall quantifier
quants = (1,)
h = HyperAutomaton(quants, label_type=pt)
h.add_vertices(4, )
h.initial_state_indices = [0]
h.add_edge(0, 1, (pt.default_value,))

h.add_edge(1, 2, (pt(is_cont="0", PC="5", con_y='true'),))

h.add_edge(2, 2, (pt(is_cont="0", PC="13", con_y='true'),))
h.add_edge(2, 2, (pt(is_cont="1", PC="13", con_y='true'),))
h.add_edge(2, 2, (pt(is_cont="0", PC="13", con_y='false'),))
h.add_edge(2, 2, (pt(is_cont="1", PC="13", con_y='false'),))

h.add_edge(2, 2, (pt(is_cont="0", PC="15", con_y='true'),))
h.add_edge(2, 2, (pt(is_cont="1", PC="15", con_y='true'),))
h.add_edge(2, 2, (pt(is_cont="0", PC="15", con_y='false'),))
h.add_edge(2, 2, (pt(is_cont="1", PC="15", con_y='false'),))

h.add_edge(2, 2, (pt(is_cont="0", PC="17", con_y='true'),))
h.add_edge(2, 2, (pt(is_cont="1", PC="17", con_y='true'),))
h.add_edge(2, 2, (pt(is_cont="0", PC="17", con_y='false'),))
h.add_edge(2, 2, (pt(is_cont="1", PC="17", con_y='false'),))

h.add_edge(2, 2, (pt(is_cont="0", PC="18", con_y='true'),))
h.add_edge(2, 2, (pt(is_cont="1", PC="18", con_y='true'),))
h.add_edge(2, 2, (pt(is_cont="0", PC="18", con_y='false'),))
h.add_edge(2, 2, (pt(is_cont="1", PC="18", con_y='false'),))

h.add_edge(2, 2, (pt(is_cont="0", PC="20", con_y='true'),))
h.add_edge(2, 2, (pt(is_cont="1", PC="20", con_y='true'),))
h.add_edge(2, 2, (pt(is_cont="0", PC="20", con_y='false'),))
h.add_edge(2, 2, (pt(is_cont="1", PC="20", con_y='false'),))


h.add_edge(2, 2, (pt(is_cont="0", PC="25", con_y='true'),))
h.add_edge(2, 2, (pt(is_cont="1", PC="25", con_y='true'),))


h.add_edge(1, 3, (pt(is_cont="0", PC="5", con_y='false'),))

h.add_edge(3, 3, (pt(is_cont="0", PC="13", con_y='true'),))
h.add_edge(3, 3, (pt(is_cont="1", PC="13", con_y='true'),))
h.add_edge(3, 3, (pt(is_cont="0", PC="13", con_y='false'),))
h.add_edge(3, 3, (pt(is_cont="1", PC="13", con_y='false'),))

h.add_edge(3, 3, (pt(is_cont="0", PC="15", con_y='true'),))
h.add_edge(3, 3, (pt(is_cont="1", PC="15", con_y='true'),))
h.add_edge(3, 3, (pt(is_cont="0", PC="15", con_y='false'),))
h.add_edge(3, 3, (pt(is_cont="1", PC="15", con_y='false'),))

h.add_edge(3, 3, (pt(is_cont="0", PC="17", con_y='true'),))
h.add_edge(3, 3, (pt(is_cont="1", PC="17", con_y='true'),))
h.add_edge(3, 3, (pt(is_cont="0", PC="17", con_y='false'),))
h.add_edge(3, 3, (pt(is_cont="1", PC="17", con_y='false'),))

h.add_edge(3, 3, (pt(is_cont="0", PC="18", con_y='true'),))
h.add_edge(3, 3, (pt(is_cont="1", PC="18", con_y='true'),))
h.add_edge(3, 3, (pt(is_cont="0", PC="18", con_y='false'),))
h.add_edge(3, 3, (pt(is_cont="1", PC="18", con_y='false'),))

h.add_edge(3, 3, (pt(is_cont="0", PC="20", con_y='true'),))
h.add_edge(3, 3, (pt(is_cont="1", PC="20", con_y='true'),))
h.add_edge(3, 3, (pt(is_cont="0", PC="20", con_y='false'),))
h.add_edge(3, 3, (pt(is_cont="1", PC="20", con_y='false'),))



h.add_edge(3, 3, (pt(is_cont="0", PC="25", con_y='true'),))
h.add_edge(3, 3, (pt(is_cont="1", PC="25", con_y='true'),))
#
#
#
def _run_cont_synth(plant, h):
    prob = ControllerSynthesisEncodingQBF(plant, h, do_optimization=True)
    prob.encode()
    output = prob.solve()
    if output.is_error:
        raise RuntimeError('Solver error: ', output.msg)
    controller = prob.decode_controller(output.model)
    return controller


c1 = _run_cont_synth(plant, h)

if(str(c1) != 'None'):
    print('controller found')
    print(type(c1))
    print(c1)
    print(c1.vs['label'])
    state_num = (c1.vs['name'])
    c = 0
    for l in (c1.vs['label']):
      print(str(state_num[c]) + ' :  ' + str(l))
      c += 1

else:
    print('controller not found.')
