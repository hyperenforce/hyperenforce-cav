from time import time

from hyper_synth.automata import Plant
from hyper_synth.datatype import DataType
from hyper_synth.qbf_encoding import ControllerSynthesisEncodingQBF
from obfuscation.obfuscation_plant import create_obfuscation_plant_and_spec
from obfuscation.obfuscation_spec import *
from obfuscation.obfuscation_spec_symbolic import *

#from hyper_synth.sat_encoding import ControllerSynthesisEncodingSAT


def obf_plant(unfold_to_tree, remove_bad_inf, remove_bad_obf):
    """
    This constructs the plant where the source output, network/obfuscator output, and inferred output are all a single bit.
    """
    source_type = DataType({"source": ["a", "b"]})
    source = Plant(label_type=source_type)

    source.add_vertices(3, label=[source_type(source="a"), source_type(source="a"), source_type(source="b")])
    source.initial_state_index = 0
    source.add_edge(0, 1, Plant.euc)
    source.add_edge(0, 2, Plant.euc)

    sec_out = {"source"}
    inf_out = {"source"}
    obs_out = {"source"}

    net_names = {"source": "net"}
    inf_names = {"source": "inf"}

    plant, type_dict, spec_dict, plant_state_encoding, label_encoding, label_func\
        = create_obfuscation_plant_and_spec(source, sec_out, inf_out, obs_out,
                                            net_names=net_names,
                                            remove_bad_inf=remove_bad_inf, remove_bad_obf=remove_bad_obf)

    if unfold_to_tree:
        plant = plant.unfold_to_tree()
    return plant, type_dict, inf_names, plant_state_encoding, label_encoding, label_func

"""
def test_obfuscation_synthesis_qbf():

    t1 = time()
    plant, type_dict, inf_names, plant_state_encoding, label_encoding, label_func = obf_plant(unfold_to_tree=False,
                                                                                              remove_bad_inf=True)
    t2 = time()

    h_lin = lin_hyper_auto(type_dict, inf_names)
    h_priv = privacy_hyperautomaton(type_dict)
    h_pipe_1 = pipeline_1_hyper_auto(type_dict)
    h_pipe_2 = pipeline_2_hyper_auto(type_dict)
    t3 = time()

    # TODO - test all specifications
    prob = ControllerSynthesisEncodingQBF(plant, h_priv,
                                         #h_pipe_1, h_pipe_2,
                                          quantify_path_steps=False)
    prob.encode()
    print(len(prob.qbf.__repr__()))

    t4 = time()
    output = prob.solve()
    t5 = time()

    controller = prob.decode_controller(output.model)
    t6 = time()
    assert controller
    #controller.vs["name"] = list(zip(controller.vs.indices, controller.vs["label"]))

    print("-----------------------")
    print("Timing")
    print(f"Plant construction: {t2 - t1}")
    print(f"Specification construction: {t3 - t2}")
    print(f"SAT encoding: {t4 - t3}")
    print(f"SAT solving: {t5 - t4}")
    print(f"SAT decoding: {t6 - t5}")
    print(f"Total: {t6 - t1}")

    print("-----------------------")
    print("Plant Info")
    print(f"#Plant states: {plant.vcount()}")
    print(f"#Plant transitions: {plant.ecount()}")
    print(f"#Controller transitions: {controller.ecount()}")

    print("-----------------------")
    print("Hyperautomata Info")
    print(f"#States (linear): {h_lin.vcount()}")
    print(f"#Transitions (linear): {h_lin.ecount()}")
    print(f"#States (pipeline 1): {h_pipe_1.vcount()}")
    print(f"#Transitions (pipeline 1): {h_pipe_1.ecount()}")
    print(f"#States (pipeline 2): {h_pipe_2.vcount()}")
    print(f"#Transitions (pipeline 2): {h_pipe_2.ecount()}")
    print(f"#States (privacy): {h_priv.vcount()}")
    print(f"#Transitions (privacy): {h_priv.ecount()}")

    return controller
"""

def test_obfuscation_synthesis_qbf_symbolic():

    time()
    plant, type_dict, inf_names,\
    plant_state_encoding, label_encoding, label_func = obf_plant(unfold_to_tree=False,
                                                                 remove_bad_inf=True,
                                                                 remove_bad_obf=False)
    time()

    #lin_symbolic_hyper_auto(type_dict, inf_names, label_encoding)
    h_priv = privacy_sybmolic_hyperautomaton(type_dict, label_encoding)
    h_pipe_1 = pipeline_1_sybmolic_hyper_auto(type_dict, label_encoding)
    h_pipe_2 = pipeline_2_sybmolic_hyper_auto(type_dict, label_encoding)
    time()

    # TODO - test all specifications
    prob = ControllerSynthesisEncodingQBF(plant, h_priv, h_pipe_1, h_pipe_2,
                                          plant_state_enc=plant_state_encoding,
                                          label_enc=label_encoding,
                                          label_func=label_func,
                                          quantify_path_steps=False)
    prob.encode()

    time()
    output = prob.solve()
    time()

    controller = prob.decode_controller(output.model)
    #print(controller)

    time()
    assert controller

    return controller
