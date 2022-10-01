from hyper_synth.automata import Plant
from hyper_synth.datatype import DataType
from obfuscation.obfuscation_plant import create_obfuscation_plant_and_spec

euc = Plant.euc
ec = Plant.ec


def test_privacy_arena():
    source_type = DataType({"source": ["a", "b"]})
    source = Plant(label_type=source_type)
    source.add_vertices(3, label=[source_type.default_value, source_type(source="a"), source_type(source="b")])
    source.initial_state_index = 0
    source.add_edge(0, 1, euc)
    source.add_edge(0, 2, euc)

    sec_out = {"source"}
    inf_out = {"source"}
    obs_out = {"source"}

    plant, type_dict, spec_dict, _, _, _ = create_obfuscation_plant_and_spec(source, sec_out, inf_out, obs_out,
                                                                             remove_bad_inf=False, remove_bad_obf=False)

    assert type_dict["plant"].num_values() == 2 ** 5
    assert plant.vcount() == 41
    assert plant.ecount() == 40


    plant, type_dict, spec_dict, _, _, _ = create_obfuscation_plant_and_spec(source, sec_out, inf_out, obs_out,
                                                                             remove_bad_inf=True, remove_bad_obf=False)

    assert type_dict["plant"].num_values() == 2 ** 5
    assert plant.vcount() == 25
    assert plant.ecount() == 24
