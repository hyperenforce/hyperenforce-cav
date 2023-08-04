import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
from hyper_synth.automata import Plant
from hyper_synth.datatype import DataType
from hyper_synth.encoding import (DataTypeEncoding, SetEncoding,
                                  equal_tuple_form)
from hyper_synth.hyperautomata import (ExplicitHyperAutomaton,
                                       SymbolicHyperAutomaton)
from hyper_synth.qbf import NOT, TRUE
from hyper_synth.qbf_encoding import ControllerSynthesisEncodingQBF
from hyper_synth.qbf import *
import logging
import sys
from hyper_synth.qbf_solver import QBFSolver



solver = QBFSolver(tmp_dir_path=".", preprocessing=True)


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
pt = DataType({'is_cont': ['0', '1', 'null', ''], 'PC': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '0.0', '1.0', '2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0', '10.0', '11.0', '12.0', '13.0', '14.0', '15.0', '16.0', '17.0', '18.0', '19.0', '20.0', '21.0', '22.0', '23.0', '24.0', '25.0', '26.0', '27.0', '28.0', '29.0', '30.0', '31.0', '32.0', '33.0', '34.0', '35.0', '36.0', '37.0', '38.0', '39.0', '40.0', '41.0', '42.0', '43.0', '44.0', '45.0', '46.0', '47.0', '48.0', '49.0', '50.0', '51.0', '52.0', '53.0', '54.0', '55.0', '56.0', '57.0', '58.0', '59.0', '60.0', '61.0', '62.0', '63.0', '64.0', '65.0', '66.0', '67.0', '68.0', '69.0', '70.0', '71.0', '72.0', '73.0', '74.0', '75.0', '76.0', '77.0', '78.0', '79.0', '80.0', '81.0', '82.0', '83.0', '84.0', '85.0', '86.0', '87.0', '88.0', '89.0', '90.0', '91.0', '92.0', '93.0', '94.0', '95.0', '96.0', '97.0', '98.0', '99.0', 'null', ''], 'con_y': ['true', 'false', 'null', '']})
plant = Plant(label_type=pt)
# add an empty init state
plant.add_vertex(label=pt.default_value)
# make it initial state
plant.initial_state_index = 0

# trace 1
# ucon_x = true
# supp_0 = true
plant.add_vertex(label=pt(is_cont="0", PC="4", con_y="true")) # index:1
plant.add_uncont_edges([(0, 1)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="11", con_y="true")) # index:2
plant.add_cont_edges([(1, 2)], weight=[1])

# trace 2
# ucon_x = false
# supp_0 = false
plant.add_vertex(label=pt(is_cont="0", PC="4", con_y="false")) # index:3
plant.add_uncont_edges([(0, 3)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="11", con_y="false")) # index:4
plant.add_cont_edges([(3, 4)], weight=[1])

# trace 3
# ucon_x = true
# supp_0 = false
# repeating state at PC=4, goes back to index:3
# repeating uncontrollable edge: (0,3), ignore 
# repeating state at PC=11, goes back to index:4
# repeating controllable edge: (3,4), ignore 
#
#
#
"""
A hyper automaton: Forall Forall, observational determinism on controllable con_y
"""
# Plant output type
# Forall quantifier

pt_enc = DataTypeEncoding(pt)
quants = (2,)
h = SymbolicHyperAutomaton(quants, pt, pt_enc)

true_form = lambda v1, v2: TRUE
wait_outputs = lambda v1, v2: NOT(OR(pt_enc.encodes_var_form(v1, PC='13'),pt_enc.encodes_var_form(v2, PC='13')))
end_condition = lambda v1, v2: AND(pt_enc.same_var_form(v1, v2, 'con_y'), AND(pt_enc.encodes_var_form(v1, PC='13'),pt_enc.encodes_var_form(v2, PC='13')))


h.add_vertices(3, )
h.initial_state_indices = [0]
h.vs["marked"] = True

h.add_edge(0, 1, true_form)
h.add_edge(1, 1, wait_outputs)
h.add_edge(1, 2, end_condition)
#
#
#
def _run_cont_synth(plant, h):
    prob = ControllerSynthesisEncodingQBF(plant, h, do_optimization=True, no_deadlocks=False, quantify_path_steps=False)
    prob.encode()
    output = prob.solve()
    if output.is_error:
        raise RuntimeError('Solver error: ', output.msg)
    controller = prob.decode_controller(output.model)
    return controller


c1 = _run_cont_synth(plant, h)

if(str(c1) != 'None'):
    print('controller found!')
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
