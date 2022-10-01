import itertools


def generic_sync_compose(init, state_attr_list, state_attr_map, edge_map, *automata,
                         dest=None):
    """
    Compute a generic synchronous product of automata with provided semantics.
    The product is computed by iterating over tuples of states of the `automata` that have been reached,
    initialized with the provided states `init`.
    The attributes of the pair of states are computed by applying the provided map state_attr_map
    to the attributes in the attr_list of the states in the pair.
    Given an outgoing transition from each state in the current state tuple,
    a transition is added to the product system if it is allowed by the provided `edge_label_map`, which
    also computes the resulting label.

    Parameters
    ----------
    init : iter[tuple]
        The state to start constructing the product at (not related to "init" vertex attribute)
    state_attr_list : iter[str]
        The state attributes in the product
    state_attr_map : Callable[..., dict[str, obj]]
        The map from the attributes of state to the attributes in the product state
    edge_map : Callable[..., tuple[bool, obj]]
        The map from edges to whether the product transition is allowed and if so, the corresponding transition label
    automata : *Automata
        The automata to compose
    dest : NFA or None
        An automaton object where the composition should be stored.
        If `None`, then a new NFA is constructed.

    Returns
    -------
    NFA
        The composed automaton
    """
    g_comp = dest
    if g_comp is None:
        from hyper_synth.automata import NFA
        g_comp = NFA()
    if g_comp.vcount() != 0 or g_comp.ecount() != 0:
        raise ValueError("The composition can only be constructed in an empty automaton")
    if not init:
        return g_comp

    state_list = {}
    state_attr = {attr: [] for attr in state_attr_list}

    edge_info = []

    next_states_to_check = []

    def add_state_tuple(state_tuple):
        if state_tuple not in state_list:
            new_index = len(state_list)
            state_list[state_tuple] = new_index
            new_attr = state_attr_map(*[g.vs[state_tuple[i]] for i, g in enumerate(automata)])
            for attr in state_attr_list:
                state_attr[attr].append(new_attr[attr])
            next_states_to_check.append(state_tuple)
            return new_index
        else:
            return state_list[state_tuple]

    def add_edge_tuple(edge_tuple):
        add_edge, edge_label = edge_map(*edge_tuple)
        if add_edge:
            cur_ind = state_list[tuple(e.source for e in edge_tuple)]
            new_ind = add_state_tuple(tuple(e.target for e in edge_tuple))
            edge_info.append(((cur_ind, new_ind), edge_label))

    for init_tuple in init:
        add_state_tuple(init_tuple)

    # set next_states_to_check returns False when empty
    while next_states_to_check:
        state_tuple = next_states_to_check.pop()
        # Iterate through all new synchronized states found in last iteration, checking neighbors
        # select edges with source at current vertex
        for edge_tuple in itertools.product(*[g.es(_source=state_tuple[i]) for i, g in enumerate(automata)]):
            add_edge_tuple(edge_tuple)

    g_comp.add_vertices(len(state_list), names=list(state_list.keys()), **state_attr)
    if edge_info:
        edge_info = tuple(zip(*set(edge_info)))
        g_comp.add_edges(edge_info[0], edge_info[1])

    return g_comp


def generic_async_compose(init, state_attr_list, state_attr_map, edge_map,
                          *automata, dest=None):
    """
    Compute a generic asynchronous product of automata with provided semantics.
    The product is computed by iterating over tuples of states of the `automata` that have been reached,
    initialized with the provided states `init`.
    The attributes of the pair of states are computed by applying the provided map state_attr_map
    to the attributes in the attr_list of the states in the pair.
    Given an outgoing transition (or an added self-loop labeled `None` representing no transition)
    from each state in the current state tuple,  a transition is added to the product system if it is allowed by
    the provided `edge_label_map`, which also computes the resulting label.

    Parameters
    ----------
    init : iter[tuple]
        The state to start constructing the product at (not related to "init" vertex attribute)
    state_attr_list : iter[str]
        The list of state attributes in the product
    state_attr_map : Callable[..., dict[str, obj]]
        The map from the attributes of state to the attributes in the product state
    edge_map : Callable[..., tuple[bool, obj]]
        The map from edges to whether the product transition is allowed and if so, the corresponding transition label
        The map should also account for newly added self-loop transitions labeled None representing the component
        of the state not transitioning
    automata : *Automata
        The automata to compose

    Returns
    -------
    NFA
        The composed automaton
    """
    empty_label = None

    # Create copies of automata with new self-loops labeled by None
    async_automata = [g.copy() for g in automata]
    for g in async_automata:
        g.add_edges([(v, v) for v in g.vs.indices], [empty_label] * g.vcount())

    return generic_sync_compose(init, state_attr_list, state_attr_map, edge_map, *async_automata, dest=dest)
