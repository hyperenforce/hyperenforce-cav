from hyper_synth.automata import Plant
from hyper_synth.datatype import DataType
from hyper_synth.encoding import (DataTypeEncoding, SetEncoding,
                                  equal_tuple_form)
from hyper_synth.hyperautomata import (ExplicitHyperAutomaton,
                                       SymbolicHyperAutomaton)
from hyper_synth.qbf import AND, NOT, TRUE
from hyper_synth.qbf_encoding import ControllerSynthesisEncodingQBF

pt = DataType({'is_cont': ['0', '1', 'null'], 'PC': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', 'null'], 'con_y': ['true', 'false', 'null']})
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
plant.add_vertex(label=pt(is_cont="1", PC="17", con_y="true")) # index:3
plant.add_cont_edges([(2, 3)], weight=[1])

# trace 2
# ucon_x = false
# ucon_z = false
# supp_0 = false
plant.add_vertex(label=pt(is_cont="0", PC="5", con_y="false")) # index:4
plant.add_uncont_edges([(0, 4)], weight=[1])
plant.add_vertex(label=pt(is_cont="0", PC="13", con_y="false")) # index:5
plant.add_uncont_edges([(4, 5)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="17", con_y="false")) # index:6
plant.add_cont_edges([(5, 6)], weight=[1])

# trace 3
# ucon_x = false
# ucon_z = true
# supp_0 = false
# repeating state at PC=5, goes back to index:4
# repeating uncontrollable edge: (0,4), ignore
# repeating state at PC=13, goes back to index:5
# repeating uncontrollable edge: (4,5), ignore
# repeating state at PC=17, goes back to index:6
# repeating controllable edge: (5,6), ignore

# trace 4
# ucon_x = true
# ucon_z = false
# supp_0 = false
# repeating state at PC=5, goes back to index:4
# repeating uncontrollable edge: (0,4), ignore
# repeating state at PC=17, goes back to index:5
# repeating uncontrollable edge: (4,5), ignore
# repeating state at PC=17, goes back to index:6
# repeating controllable edge: (5,6), ignore

# trace 5
# ucon_x = true
# ucon_z = false
# supp_0 = true
# repeating state at PC=5, goes back to index:4
# repeating uncontrollable edge: (0,4), ignore
# repeating state at PC=13, goes back to index:5
# repeating uncontrollable edge: (4,5), ignore
# repeating state at PC=17, goes back to index:6
# repeating controllable edge: (5,6), ignore
#
#
#
"""
A hyper automaton
"""
# Plant output type
# Forall quantifier

pt_enc = DataTypeEncoding(pt)
quants = (2,)
h = SymbolicHyperAutomaton(quants, pt, pt_enc)
# end_condition = lambda vpt: pt_enc.encodes_var_form(vpt, PC='17', con_y='true')
# end_condition = lambda v1, v2: pt_enc.encodes_var_form(vpt, PC='17', con_y='true')

end_condition = lambda v1, v2: AND(pt_enc.encodes_var_form(v1, PC='17', con_y='true'),
                                   pt_enc.encodes_var_form(v2, PC='17', con_y='true'))
true_form = lambda v1, v2: TRUE

h.add_vertices(3, )
h.initial_state_indices = [0]
h.vs["marked"] = True


h.add_edge(0, 1, true_form)
h.add_edge(1, 1, true_form)
h.add_edge(1, 2, end_condition)
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
