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
pt = DataType({'is_cont': ['0', '1', 'null', ''], 'PC': ['5', '35', '36', '37', '38', '39', '42', '56', '83', '84', '101', '102', '103', '104', '105', '169', '170', '171', '172', '208', '213', '214', '250', '263', '284', '285', 'null', ''], 'con_str_output_hex': ['HIGH_a', 'LOW_b', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'null', '']})
plant = Plant(label_type=pt)
# add an empty init state
plant.add_vertex(label=pt.default_value)
# make it initial state
plant.initial_state_index = 0

# trace 1
# ucon_str_plainText = null
# ucon_num_hexcase = 0
# ucon_str_b64pad = null
# ucon_num_chrsz = 0
plant.add_vertex(label=pt(is_cont="0", PC="5", con_str_output_hex="0")) # index:1
plant.add_uncont_edges([(0, 1)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="35", con_str_output_hex="0")) # index:2
plant.add_cont_edges([(1, 2)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="36", con_str_output_hex="0")) # index:3
plant.add_cont_edges([(2, 3)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="37", con_str_output_hex="0")) # index:4
plant.add_cont_edges([(3, 4)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="38", con_str_output_hex="0")) # index:5
plant.add_cont_edges([(4, 5)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="39", con_str_output_hex="0")) # index:6
plant.add_cont_edges([(5, 6)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="42", con_str_output_hex="0")) # index:7
plant.add_cont_edges([(6, 7)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="56", con_str_output_hex="0")) # index:8
plant.add_cont_edges([(7, 8)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="83", con_str_output_hex="0")) # index:9
plant.add_cont_edges([(8, 9)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="84", con_str_output_hex="0")) # index:10
plant.add_cont_edges([(9, 10)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="101", con_str_output_hex="0")) # index:11
plant.add_cont_edges([(10, 11)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="102", con_str_output_hex="0")) # index:12
plant.add_cont_edges([(11, 12)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="103", con_str_output_hex="0")) # index:13
plant.add_cont_edges([(12, 13)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="104", con_str_output_hex="0")) # index:14
plant.add_cont_edges([(13, 14)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="105", con_str_output_hex="0")) # index:15
plant.add_cont_edges([(14, 15)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="169", con_str_output_hex="0")) # index:16
plant.add_cont_edges([(15, 16)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="170", con_str_output_hex="0")) # index:17
plant.add_cont_edges([(16, 17)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="171", con_str_output_hex="0")) # index:18
plant.add_cont_edges([(17, 18)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="172", con_str_output_hex="0")) # index:19
plant.add_cont_edges([(18, 19)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="208", con_str_output_hex="0")) # index:20
plant.add_cont_edges([(19, 20)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="213", con_str_output_hex="0")) # index:21
plant.add_cont_edges([(20, 21)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="214", con_str_output_hex="0")) # index:22
plant.add_cont_edges([(21, 22)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="250", con_str_output_hex="0")) # index:23
plant.add_cont_edges([(22, 23)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="263", con_str_output_hex="0")) # index:24
plant.add_cont_edges([(23, 24)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="284", con_str_output_hex="0")) # index:25
plant.add_cont_edges([(24, 25)], weight=[1])
plant.add_vertex(label=pt(is_cont="1", PC="285", con_str_output_hex="0")) # index:26
plant.add_cont_edges([(25, 26)], weight=[1])
#
#
#
"""
A hyper automaton Forall pi Forall pi'. if input text matches, then the output hex must also match
"""
# Plant output type
# Forall quantifier

pt_enc = DataTypeEncoding(pt)
quants = (2,)
h = SymbolicHyperAutomaton(quants, pt, pt_enc)

true_form = lambda v1, v2: TRUE
inputs_match = lambda v1, v2: lambda v1, v2: (pt_enc.same_var_form(v1, v2, 'ucon_str_plainText'))
wait_outputs = lambda v1, v2: NOT(OR(pt_enc.encodes_var_form(v1, PC='285'), pt_enc.encodes_var_form(v2, PC='285')))
end_condition = lambda v1, v2: AND(pt_enc.same_var_form(v1, v2, 'con_str_output_hex'), AND(pt_enc.encodes_var_form(v1, PC='285'),pt_enc.encodes_var_form(v2, PC='285')))


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
