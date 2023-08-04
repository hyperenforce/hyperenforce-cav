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
pt = DataType({'is_cont': ['0', '1', 'null', ''], 'PC': ['5', '15', '19', '30', '32', '36', '38', 'null', ''], 'con_str_baseUrl': ['mysite.com/intern/login.php', 'mysite.com/login.php', "'mysite.com/intern/login.php'", "'mysite.com/login.php'", 'null', '']})
plant = Plant(label_type=pt)
# add an empty init state
plant.add_vertex(label=pt.default_value)
# make it initial state
plant.initial_state_index = 0

# trace 1
# ucon_str_cookie = isIntern
# supp_0 = true
# ucon_select = true
plant.add_vertex(label=pt(is_cont="0", PC="5", con_str_baseUrl="mysite.com/intern/login.php")) # index:1
plant.add_cont_edges([(0, 1)], weight=[1])
plant.add_vertex(label=pt(is_cont="0", PC="15", con_str_baseUrl="mysite.com/intern/login.php")) # index:2
plant.add_uncont_edges([(1, 2)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="19", con_str_baseUrl="mysite.com/intern/login.php")) # index:3
# repeating controllable edge: (2,2), ignore 
plant.add_vertex(label=pt(is_cont="1", PC="30", con_str_baseUrl="mysite.com/intern/login.php")) # index:4
# repeating controllable edge: (2,2), ignore 
plant.add_vertex(label=pt(is_cont="1", PC="32", con_str_baseUrl="mysite.com/intern/login.php")) # index:5
# repeating controllable edge: (2,2), ignore 
plant.add_vertex(label=pt(is_cont="1", PC="36", con_str_baseUrl="mysite.com/intern/login.php")) # index:6
plant.add_cont_edges([(2, 6)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="38", con_str_baseUrl="mysite.com/intern/login.php")) # index:7
plant.add_cont_edges([(6, 7)], weight=[1])

# trace 2
# ucon_str_cookie = 
# supp_0 = false
# ucon_select = false
plant.add_vertex(label=pt(is_cont="0", PC="5", con_str_baseUrl="")) # index:8
plant.add_cont_edges([(0, 8)], weight=[1])
plant.add_vertex(label=pt(is_cont="0", PC="15", con_str_baseUrl="")) # index:9
# repeating uncontrollable edge: (8,8), ignore 
plant.add_vertex(label=pt(is_cont="1", PC="19", con_str_baseUrl="")) # index:10
# repeating controllable edge: (8,8), ignore 
plant.add_vertex(label=pt(is_cont="1", PC="30", con_str_baseUrl="")) # index:11
# repeating controllable edge: (8,8), ignore 
plant.add_vertex(label=pt(is_cont="1", PC="32", con_str_baseUrl="")) # index:12
# repeating controllable edge: (8,8), ignore 
plant.add_vertex(label=pt(is_cont="1", PC="36", con_str_baseUrl="")) # index:13
plant.add_cont_edges([(8, 13)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="38", con_str_baseUrl="'mysite.com/login.php'")) # index:14
plant.add_cont_edges([(13, 14)], weight=[1])

# trace 3
# ucon_str_cookie = 
# supp_0 = false
# ucon_select = true
plant.add_vertex(label=pt(is_cont="0", PC="5", con_str_baseUrl="")) # index:15
plant.add_cont_edges([(0, 15)], weight=[1])
# repeating state at PC=15, goes back to index:9
plant.add_uncont_edges([(15, 9)], weight=[1])
# repeating state at PC=36, goes back to index:10
plant.add_cont_edges([(9, 10)], weight=[1])
# repeating state at PC=36, goes back to index:11
plant.add_cont_edges([(10, 11)], weight=[1])
# repeating state at PC=36, goes back to index:12
plant.add_cont_edges([(11, 12)], weight=[1])
# repeating state at PC=36, goes back to index:13
plant.add_cont_edges([(12, 13)], weight=[1])
# repeating state at PC=38, goes back to index:14
# repeating controllable edge: (13,14), ignore 

# trace 4
# ucon_str_cookie = isIntern
# supp_0 = false
# ucon_select = false
plant.add_vertex(label=pt(is_cont="0", PC="5", con_str_baseUrl="")) # index:16
plant.add_cont_edges([(0, 16)], weight=[1])
# repeating state at PC=30, goes back to index:9
plant.add_uncont_edges([(16, 9)], weight=[1])
# repeating state at PC=30, goes back to index:10
# repeating controllable edge: (9,10), ignore 
# repeating state at PC=30, goes back to index:11
# repeating controllable edge: (10,11), ignore 
plant.add_vertex(label=pt(is_cont="1", PC="32", con_str_baseUrl="'mysite.com/intern/login.php'")) # index:17
plant.add_cont_edges([(11, 17)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="36", con_str_baseUrl="'mysite.com/intern/login.php'")) # index:18
plant.add_cont_edges([(17, 18)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="38", con_str_baseUrl="'mysite.com/intern/login.php'")) # index:19
plant.add_cont_edges([(18, 19)], weight=[1])

# trace 5
# ucon_str_cookie = isIntern
# supp_0 = true
# ucon_select = false
plant.add_vertex(label=pt(is_cont="0", PC="5", con_str_baseUrl="")) # index:20
plant.add_cont_edges([(0, 20)], weight=[1])
# repeating state at PC=30, goes back to index:9
plant.add_uncont_edges([(20, 9)], weight=[1])
# repeating state at PC=30, goes back to index:10
# repeating controllable edge: (9,10), ignore 
# repeating state at PC=30, goes back to index:11
# repeating controllable edge: (10,11), ignore 
# repeating state at PC=32, goes back to index:12
# repeating controllable edge: (11,12), ignore 
# repeating state at PC=36, goes back to index:13
# repeating controllable edge: (12,13), ignore 
plant.add_vertex(label=pt(is_cont="1", PC="38", con_str_baseUrl="")) # index:21
plant.add_cont_edges([(13, 21)], weight=[1])

# trace 6
# ucon_str_cookie = 
# supp_0 = true
# ucon_select = false
plant.add_vertex(label=pt(is_cont="0", PC="5", con_str_baseUrl="")) # index:22
plant.add_cont_edges([(0, 22)], weight=[1])
# repeating state at PC=36, goes back to index:9
plant.add_uncont_edges([(22, 9)], weight=[1])
# repeating state at PC=36, goes back to index:10
# repeating controllable edge: (9,10), ignore 
# repeating state at PC=36, goes back to index:11
# repeating controllable edge: (10,11), ignore 
# repeating state at PC=36, goes back to index:12
# repeating controllable edge: (11,12), ignore 
# repeating state at PC=36, goes back to index:13
# repeating controllable edge: (12,13), ignore 
# repeating state at PC=38, goes back to index:21
# repeating controllable edge: (13,21), ignore 

#
#
"""
A hyper automaton Forall Forall, if username (cookie) match, then DOM should always match.
"""
# Plant output type
# Forall quantifier

pt_enc = DataTypeEncoding(pt)
quants = (1,1)
h = SymbolicHyperAutomaton(quants, pt, pt_enc)

true_form = lambda v1, v2: TRUE
# inputs_match = lambda v1, v2: lambda v1, v2: (pt_enc.same_var_form(v1, v2, 'ucon_str_cookie'))
# wait_outputs = lambda v1, v2: NOT(OR(pt_enc.encodes_var_form(v1, PC='48'),pt_enc.encodes_var_form(v2, PC='48')))
end_condition = lambda v1, v2: AND(AND(pt_enc.same_var_form(v1, v2, 'con_num_latitude'), pt_enc.same_var_form(v1, v2, 'con_num_longitude')), AND(pt_enc.encodes_var_form(v1, PC='72'),pt_enc.encodes_var_form(v2, PC='72')))


h.add_vertices(3, )
h.initial_state_indices = [0]
h.vs["marked"] = True

h.add_edge(0, 1, true_form)
h.add_edge(1, 2, true_form)
h.add_edge(2, 2, true_form)
# h.add_edge(1, 2, end_condition)
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
