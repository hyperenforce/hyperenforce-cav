from hyper_synth.automata import Plant
from hyper_synth.datatype import DataType

euc = Plant.euc
ec = Plant.ec

def uncont_auto_1():
    label_type = DataType({"t1": ['a', 'b']})
    g = Plant(label_type=label_type)
    g.add_vertices(3, label=[label_type(t1='a'), label_type(t1='a'), label_type(t1='b')])
    g.initial_state_index = 0
    g.add_edges([(0, 1), (0, 2)], [euc, euc])
    return g


def uncont_auto_2():
    label_type = DataType({"t2": ['c', 'd']})
    g = Plant(label_type=label_type)
    g.add_vertices(2, label=[label_type(t2='c'), label_type(t2='d')])
    g.initial_state_index = 0
    g.add_edges([(0, 1), (1, 0)], [euc, euc])
    return g


def cont_auto_1():
    label_type = DataType({"tc": ['e', 'f']})
    g = Plant(label_type=label_type)
    g.add_vertices(3, label=[label_type(tc='e'), label_type(tc='e'), label_type(tc='f')])
    g.initial_state_index = 0
    g.add_edges([(0, 1), (0, 2)], [ec, ec])
    return g


def test_sync_compose_type():
    g1 = uncont_auto_1()
    g2 = uncont_auto_2()
    gp = g1.sync_compose(g2)
    tp = gp.label_type

    assert tp.num_values() == 4
    assert gp.vcount() == 3
    assert gp.ecount() == 2
    assert set(e.target_vertex["label"] for e in gp.es) == {tp(t1='a', t2='d'), tp(t1='b', t2='d')}


def test_alternating_compose_type():
    g1 = uncont_auto_1()
    g2 = uncont_auto_2()
    gp = g1.sync_compose(g2)

    g3 = cont_auto_1()
    ga = gp.alternating_compose(g3)
    ta = ga.label_type

    assert ta.num_values() == 8
    assert ga.vcount() == 7
    assert ga.ecount() == 6
    assert set(e.target_vertex["label"] for e in ga.es) == {ta(t1='a', t2='d', tc='e'), ta(t1='b', t2='d', tc='e'),
                                                            ta(t1='a', t2='d', tc='f'), ta(t1='b', t2='d', tc='f')}
