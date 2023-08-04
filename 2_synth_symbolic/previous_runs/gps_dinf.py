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
pt = DataType({'is_cont': ['0', '1', 'null', ''], 'PC': ['5', '18', '19', '22', '23', '26', '27', '55', '56', '57', '58', '59', '60', '63', '72', 'null', ''], 'con_num_longitude': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', 'null', ''], 'con_num_latitude': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', 'null', '']})
plant = Plant(label_type=pt)
# add an empty init state
plant.add_vertex(label=pt.default_value)
# make it initial state
plant.initial_state_index = 0

# trace 1
# ucon_str_cookie = 
# supp_0 = true
# ucon_num_lo = 12.3748
# ucon_num_la = 27.23501
# ucon_random_flag = true
plant.add_vertex(label=pt(is_cont="0", PC="5", con_num_longitude="0", con_num_latitude="0")) # index:1
plant.add_cont_edges([(0, 1)], weight=[1])
plant.add_vertex(label=pt(is_cont="0", PC="18", con_num_longitude="0", con_num_latitude="0")) # index:2
# repeating uncontrollable edge: (1,1), ignore 
plant.add_vertex(label=pt(is_cont="0", PC="19", con_num_longitude="0", con_num_latitude="0")) # index:3
# repeating uncontrollable edge: (1,1), ignore 
plant.add_vertex(label=pt(is_cont="0", PC="22", con_num_longitude="0", con_num_latitude="0")) # index:4
# repeating uncontrollable edge: (1,1), ignore 
plant.add_vertex(label=pt(is_cont="0", PC="23", con_num_longitude="0", con_num_latitude="0")) # index:5
# repeating uncontrollable edge: (1,1), ignore 
plant.add_vertex(label=pt(is_cont="0", PC="26", con_num_longitude="0", con_num_latitude="0")) # index:6
plant.add_uncont_edges([(1, 6)], weight=[1])
plant.add_vertex(label=pt(is_cont="0", PC="27", con_num_longitude="0", con_num_latitude="0")) # index:7
plant.add_uncont_edges([(6, 7)], weight=[1])
plant.add_vertex(label=pt(is_cont="0", PC="55", con_num_longitude="0", con_num_latitude="0")) # index:8
plant.add_uncont_edges([(7, 8)], weight=[1])
plant.add_vertex(label=pt(is_cont="0", PC="56", con_num_longitude="0", con_num_latitude="0")) # index:9
plant.add_uncont_edges([(8, 9)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="57", con_num_longitude="0", con_num_latitude="0")) # index:10
plant.add_cont_edges([(9, 10)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="58", con_num_longitude="0", con_num_latitude="0")) # index:11
plant.add_cont_edges([(10, 11)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="59", con_num_longitude="0", con_num_latitude="0")) # index:12
plant.add_cont_edges([(11, 12)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="60", con_num_longitude="0", con_num_latitude="0")) # index:13
plant.add_cont_edges([(12, 13)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="63", con_num_longitude="0", con_num_latitude="0")) # index:14
plant.add_cont_edges([(13, 14)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="72", con_num_longitude="0", con_num_latitude="0")) # index:15
plant.add_cont_edges([(14, 15)], weight=[1])

# trace 2
# ucon_str_cookie = GPS_tracking_enabled
# supp_0 = false
# ucon_num_lo = 0
# ucon_num_la = 0
# ucon_random_flag = false
plant.add_vertex(label=pt(is_cont="0", PC="5", con_num_longitude="0", con_num_latitude="0")) # index:16
plant.add_cont_edges([(0, 16)], weight=[1])
# repeating state at PC=22, goes back to index:2
plant.add_uncont_edges([(16, 2)], weight=[1])
# repeating state at PC=22, goes back to index:3
plant.add_uncont_edges([(2, 3)], weight=[1])
# repeating state at PC=22, goes back to index:4
plant.add_uncont_edges([(3, 4)], weight=[1])
# repeating state at PC=23, goes back to index:5
plant.add_uncont_edges([(4, 5)], weight=[1])
# repeating state at PC=26, goes back to index:6
plant.add_uncont_edges([(5, 6)], weight=[1])
# repeating state at PC=27, goes back to index:7
# repeating uncontrollable edge: (6,7), ignore 
# repeating state at PC=55, goes back to index:8
# repeating uncontrollable edge: (7,8), ignore 
# repeating state at PC=56, goes back to index:9
# repeating uncontrollable edge: (8,9), ignore 
# repeating state at PC=57, goes back to index:10
# repeating controllable edge: (9,10), ignore 
# repeating state at PC=58, goes back to index:11
# repeating controllable edge: (10,11), ignore 
# repeating state at PC=59, goes back to index:12
# repeating controllable edge: (11,12), ignore 
# repeating state at PC=60, goes back to index:13
# repeating controllable edge: (12,13), ignore 
# repeating state at PC=63, goes back to index:14
# repeating controllable edge: (13,14), ignore 
# repeating state at PC=72, goes back to index:15
# repeating controllable edge: (14,15), ignore 

# trace 3
# ucon_str_cookie = 
# supp_0 = false
# ucon_num_lo = 0
# ucon_num_la = 0
# ucon_random_flag = false
plant.add_vertex(label=pt(is_cont="0", PC="5", con_num_longitude="0", con_num_latitude="0")) # index:17
plant.add_cont_edges([(0, 17)], weight=[1])
# repeating state at PC=18, goes back to index:2
plant.add_uncont_edges([(17, 2)], weight=[1])
# repeating state at PC=19, goes back to index:3
# repeating uncontrollable edge: (2,3), ignore 
# repeating state at PC=22, goes back to index:4
# repeating uncontrollable edge: (3,4), ignore 
# repeating state at PC=23, goes back to index:5
# repeating uncontrollable edge: (4,5), ignore 
# repeating state at PC=26, goes back to index:6
# repeating uncontrollable edge: (5,6), ignore 
# repeating state at PC=27, goes back to index:7
# repeating uncontrollable edge: (6,7), ignore 
# repeating state at PC=55, goes back to index:8
# repeating uncontrollable edge: (7,8), ignore 
# repeating state at PC=56, goes back to index:9
# repeating uncontrollable edge: (8,9), ignore 
# repeating state at PC=57, goes back to index:10
# repeating controllable edge: (9,10), ignore 
# repeating state at PC=58, goes back to index:11
# repeating controllable edge: (10,11), ignore 
# repeating state at PC=59, goes back to index:12
# repeating controllable edge: (11,12), ignore 
# repeating state at PC=60, goes back to index:13
# repeating controllable edge: (12,13), ignore 
# repeating state at PC=63, goes back to index:14
# repeating controllable edge: (13,14), ignore 
# repeating state at PC=72, goes back to index:15
# repeating controllable edge: (14,15), ignore 

# trace 4
# ucon_str_cookie = GPS_tracking_enabled
# supp_0 = true
# ucon_num_lo = 0
# ucon_num_la = 0
# ucon_random_flag = false
plant.add_vertex(label=pt(is_cont="0", PC="5", con_num_longitude="0", con_num_latitude="0")) # index:18
plant.add_cont_edges([(0, 18)], weight=[1])
# repeating state at PC=22, goes back to index:2
plant.add_uncont_edges([(18, 2)], weight=[1])
# repeating state at PC=22, goes back to index:3
# repeating uncontrollable edge: (2,3), ignore 
# repeating state at PC=22, goes back to index:4
# repeating uncontrollable edge: (3,4), ignore 
# repeating state at PC=23, goes back to index:5
# repeating uncontrollable edge: (4,5), ignore 
# repeating state at PC=26, goes back to index:6
# repeating uncontrollable edge: (5,6), ignore 
# repeating state at PC=27, goes back to index:7
# repeating uncontrollable edge: (6,7), ignore 
# repeating state at PC=55, goes back to index:8
# repeating uncontrollable edge: (7,8), ignore 
# repeating state at PC=56, goes back to index:9
# repeating uncontrollable edge: (8,9), ignore 
# repeating state at PC=57, goes back to index:10
# repeating controllable edge: (9,10), ignore 
# repeating state at PC=58, goes back to index:11
# repeating controllable edge: (10,11), ignore 
# repeating state at PC=59, goes back to index:12
# repeating controllable edge: (11,12), ignore 
# repeating state at PC=60, goes back to index:13
# repeating controllable edge: (12,13), ignore 
# repeating state at PC=63, goes back to index:14
# repeating controllable edge: (13,14), ignore 
# repeating state at PC=72, goes back to index:15
# repeating controllable edge: (14,15), ignore 

# trace 5
# ucon_str_cookie = GPS_tracking_enabled
# supp_0 = false
# ucon_num_lo = 0
# ucon_num_la = 0
# ucon_random_flag = true
plant.add_vertex(label=pt(is_cont="0", PC="5", con_num_longitude="0", con_num_latitude="0")) # index:19
plant.add_cont_edges([(0, 19)], weight=[1])
# repeating state at PC=18, goes back to index:2
plant.add_uncont_edges([(19, 2)], weight=[1])
# repeating state at PC=19, goes back to index:3
# repeating uncontrollable edge: (2,3), ignore 
# repeating state at PC=22, goes back to index:4
# repeating uncontrollable edge: (3,4), ignore 
# repeating state at PC=23, goes back to index:5
# repeating uncontrollable edge: (4,5), ignore 
# repeating state at PC=26, goes back to index:6
# repeating uncontrollable edge: (5,6), ignore 
# repeating state at PC=27, goes back to index:7
# repeating uncontrollable edge: (6,7), ignore 
# repeating state at PC=55, goes back to index:8
# repeating uncontrollable edge: (7,8), ignore 
# repeating state at PC=56, goes back to index:9
# repeating uncontrollable edge: (8,9), ignore 
# repeating state at PC=57, goes back to index:10
# repeating controllable edge: (9,10), ignore 
# repeating state at PC=58, goes back to index:11
# repeating controllable edge: (10,11), ignore 
# repeating state at PC=59, goes back to index:12
# repeating controllable edge: (11,12), ignore 
# repeating state at PC=60, goes back to index:13
# repeating controllable edge: (12,13), ignore 
# repeating state at PC=63, goes back to index:14
# repeating controllable edge: (13,14), ignore 
# repeating state at PC=72, goes back to index:15
# repeating controllable edge: (14,15), ignore 

# trace 6
# ucon_str_cookie = GPS_tracking_enabled
# supp_0 = true
# ucon_num_lo = 0
# ucon_num_la = 0
# ucon_random_flag = true
plant.add_vertex(label=pt(is_cont="0", PC="5", con_num_longitude="0", con_num_latitude="0")) # index:20
plant.add_cont_edges([(0, 20)], weight=[1])
# repeating state at PC=18, goes back to index:2
plant.add_uncont_edges([(20, 2)], weight=[1])
# repeating state at PC=19, goes back to index:3
# repeating uncontrollable edge: (2,3), ignore 
# repeating state at PC=22, goes back to index:4
# repeating uncontrollable edge: (3,4), ignore 
# repeating state at PC=23, goes back to index:5
# repeating uncontrollable edge: (4,5), ignore 
# repeating state at PC=26, goes back to index:6
# repeating uncontrollable edge: (5,6), ignore 
# repeating state at PC=27, goes back to index:7
# repeating uncontrollable edge: (6,7), ignore 
# repeating state at PC=55, goes back to index:8
# repeating uncontrollable edge: (7,8), ignore 
# repeating state at PC=56, goes back to index:9
# repeating uncontrollable edge: (8,9), ignore 
# repeating state at PC=57, goes back to index:10
# repeating controllable edge: (9,10), ignore 
# repeating state at PC=58, goes back to index:11
# repeating controllable edge: (10,11), ignore 
# repeating state at PC=59, goes back to index:12
# repeating controllable edge: (11,12), ignore 
# repeating state at PC=60, goes back to index:13
# repeating controllable edge: (12,13), ignore 
# repeating state at PC=63, goes back to index:14
# repeating controllable edge: (13,14), ignore 
# repeating state at PC=72, goes back to index:15
# repeating controllable edge: (14,15), ignore 
#
#
#
"""
A hyper automaton Forall Exists, if declassify, we check if GPS_pi=GPS_pi' with absence of addnode (non-inference)
"""
# Plant output type
# Forall quantifier

pt_enc = DataTypeEncoding(pt)
quants = (1,1)
h = SymbolicHyperAutomaton(quants, pt, pt_enc)

true_form = lambda v1, v2: TRUE
wait_outputs = lambda v1, v2: NOT(OR(pt_enc.encodes_var_form(v1, PC='72'),pt_enc.encodes_var_form(v2, PC='72')))
# match_condition = lambda v1, v2: AND(AND(pt_enc.same_var_form(v1, v2, 'ucon_str_cookie)))
end_condition = lambda v1, v2: AND(AND(pt_enc.same_var_form(v1, v2, 'con_num_latitude'), pt_enc.same_var_form(v1, v2, 'con_num_longitude')), AND(pt_enc.encodes_var_form(v1, PC='72'),pt_enc.encodes_var_form(v2, PC='72')))


h.add_vertices(4, )
h.initial_state_indices = [0]
h.vs["marked"] = True

h.add_edge(0, 1, true_form)
h.add_edge(1, 1, wait_outputs)
h.add_edge(1, 2, true_form)
h.add_edge(2, 2, end_condition)
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
