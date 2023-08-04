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
pt = DataType({'is_cont': ['0', '1', 'null', ''], 'PC': ['5', '9', '10', '11', '12', '15', '18', '52', '53', '54', '55', '56', '57', '59', '60', '61', '62', '63', 'null', '']})
plant = Plant(label_type=pt)
# add an empty init state
plant.add_vertex(label=pt.default_value)
# make it initial state
plant.initial_state_index = 0

# trace 1
plant.add_vertex(label=pt(is_cont="0", PC="5")) # index:1
plant.add_cont_edges([(0, 1)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="9")) # index:2
plant.add_cont_edges([(1, 2)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="10")) # index:3
plant.add_cont_edges([(2, 3)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="11")) # index:4
plant.add_cont_edges([(3, 4)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="12")) # index:5
plant.add_cont_edges([(4, 5)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="15")) # index:6
plant.add_cont_edges([(5, 6)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="18")) # index:7
plant.add_cont_edges([(6, 7)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="52")) # index:8
plant.add_cont_edges([(7, 8)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="53")) # index:9
plant.add_cont_edges([(8, 9)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="54")) # index:10
plant.add_cont_edges([(9, 10)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="55")) # index:11
plant.add_cont_edges([(10, 11)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="56")) # index:12
plant.add_cont_edges([(11, 12)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="57")) # index:13
plant.add_cont_edges([(12, 13)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="59")) # index:14
plant.add_cont_edges([(13, 14)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="60")) # index:15
plant.add_cont_edges([(14, 15)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="61")) # index:16
plant.add_cont_edges([(15, 16)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="62")) # index:17
plant.add_cont_edges([(16, 17)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="63")) # index:18
plant.add_cont_edges([(17, 18)], weight=[1])

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
