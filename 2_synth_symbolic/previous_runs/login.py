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



solver = QBFSolver(tmp_dir_path=".")
solver = QBFSolver(tmp_dir_path=".", preprocessing=True)

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
pt = DataType({'is_cont': ['0', '1', 'null', ''], 'PC': ['5', '43', '44', '47', '48', '55', '56', 'null', ''], 'con_baseUrl': ['null', 'null', '']})
plant = Plant(label_type=pt)
# add an empty init state
plant.add_vertex(label=pt.default_value)
# make it initial state
plant.initial_state_index = 0

# trace 1
# ucon_cookie = null
plant.add_vertex(label=pt(is_cont="0", PC="5", con_baseUrl="null")) # index:1
plant.add_cont_edges([(0, 1)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="43", con_baseUrl="'mysite.com/login.php'")) # index:2
# repeating controllable edge: (1,1), ignore 
plant.add_vertex(label=pt(is_cont="1", PC="44", con_baseUrl="'mysite.com/login.php'")) # index:3
# repeating controllable edge: (1,1), ignore 
plant.add_vertex(label=pt(is_cont="1", PC="47", con_baseUrl="'mysite.com/login.php'")) # index:4
# repeating controllable edge: (1,1), ignore 
plant.add_vertex(label=pt(is_cont="1", PC="48", con_baseUrl="'mysite.com/login.php'")) # index:5
plant.add_cont_edges([(1, 5)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="55", con_baseUrl="'mysite.com/login.php'")) # index:6
# repeating controllable edge: (5,5), ignore 
plant.add_vertex(label=pt(is_cont="1", PC="56", con_baseUrl="'mysite.com/login.php'")) # index:7
plant.add_cont_edges([(5, 7)], weight=[1])

# trace 2
# ucon_cookie = isIntern
plant.add_vertex(label=pt(is_cont="0", PC="5", con_baseUrl="")) # index:8
plant.add_cont_edges([(0, 8)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="43", con_baseUrl="'mysite.com/intern/login.php'")) # index:9
# repeating controllable edge: (8,8), ignore 
plant.add_vertex(label=pt(is_cont="1", PC="44", con_baseUrl="'mysite.com/intern/login.php'")) # index:10
plant.add_cont_edges([(8, 10)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="47", con_baseUrl="'mysite.com/intern/login.php'")) # index:11
# repeating controllable edge: (10,10), ignore 
plant.add_vertex(label=pt(is_cont="1", PC="48", con_baseUrl="'mysite.com/intern/login.php'")) # index:12
# repeating controllable edge: (10,10), ignore 
plant.add_vertex(label=pt(is_cont="1", PC="55", con_baseUrl="'mysite.com/intern/login.php'")) # index:13
# repeating controllable edge: (10,10), ignore 
plant.add_vertex(label=pt(is_cont="1", PC="56", con_baseUrl="'mysite.com/intern/login.php'")) # index:14
plant.add_cont_edges([(10, 14)], weight=[1])
#
#
#
"""
A hyper automaton
"""
# Plant output type
# Forall quantifier

pt_enc = DataTypeEncoding(pt)
quants = (1,1)
h = SymbolicHyperAutomaton(quants, pt, pt_enc)

true_form = lambda v1, v2: TRUE
wait_outputs = lambda v1, v2: NOT(OR(pt_enc.encodes_var_form(v1, PC='72'),pt_enc.encodes_var_form(v2, PC='72')))
end_condition = lambda v1, v2: AND(pt_enc.same_var_form(v1, v2, 'con_latitude'), AND(pt_enc.encodes_var_form(v1, PC='72'),pt_enc.encodes_var_form(v2, PC='72')))


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
    # print(type(c1))
    # print(c1)
    print(c1.vs['label'])
    state_num = (c1.vs['name'])
    c = 0
    for l in (c1.vs['label']):
      print(str(state_num[c]) + ' :  ' + str(l))
      c += 1

else:
    print('controller not found.')
