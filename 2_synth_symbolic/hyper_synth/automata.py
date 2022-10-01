import DESops as d
from hyper_synth.compose import generic_async_compose, generic_sync_compose
from hyper_synth.datatype import DataType, empty_type, empty_value


class Automaton(d.NFA):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def initial_states(self):
        return self.vs.select(init=True)

    @property
    def initial_state_indices(self):
        return self.initial_states.indices

    @initial_state_indices.setter
    def initial_state_indices(self, init_indices):
        self.vs["init"] = False
        self.vs.select(init_indices)["init"] = True

    def write_svg(self, path, *args, **kwargs):
        d.write_svg(path, self, *args, **kwargs)

    def write_dot_f(self, path, *args, **kwargs):
        nfa_copy = self.copy()

        def process_attr(v):
            if isinstance(v, int) or isinstance(v, bool):
                return v
            else:
                return str(v)

        for vattr in nfa_copy.vs.attribute_names():
            if vattr != "out":
                nfa_copy.vs[vattr] = [process_attr(v) for v in nfa_copy.vs[vattr]]
        for eattr in nfa_copy.es.attribute_names():
            nfa_copy.es[eattr] = [process_attr(v) for v in nfa_copy.es[eattr]]

        nfa_copy.write_dot(path, *args, **kwargs)

    def is_tree(self):
        """
        Determine if the given plant is a tree.
        This does not allow for unconnected components.
        This does not allow for self-loops.
        """
        return self._graph.is_tree()

    def is_dag(self):
        """
        Determine if the given plant is a DAG.
        This allows for unconnected components.
        This does not allow for self-loops.
        """
        return self._graph.is_dag()

    def diameter(self):
        return self._graph.diameter()


class SingleInitialStateAutomaton(Automaton):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def initial_state(self):
        return self.vs.select(init=True)[0]

    @property
    def initial_state_index(self):
        return self.initial_state.index

    @initial_state_index.setter
    def initial_state_index(self, init_index):
        self.initial_state_indices = [init_index]

    @Automaton.initial_state_indices.setter
    def initial_state_indices(self, init_indices):
        assert len(init_indices) == 1
        Automaton.initial_state_indices.fset(self, init_indices)


class Plant(SingleInitialStateAutomaton):
    ec = "ec"
    euc = "euc"

    def __init__(self, label_type=None, name_type=None, **kwargs):
        super().__init__(**kwargs)
        self.label_type = label_type
        self.name_type = name_type
        self.Euc = {Plant.euc}

    def add_vertex(self, label=None, **kwargs):
        if label is None:
            raise ValueError("Label required for Plant vertices")
        return super().add_vertex(label=label, **kwargs)

    def add_vertices(self, num_vertices, label=None, **kwargs):
        if label is None:
            raise ValueError("Label required for Plant vertices")
        return super().add_vertices(num_vertices, label=label, **kwargs)

    @property
    def uncont_edges(self):
        return self.es.select(label=Plant.euc)

    @property
    def cont_edges(self):
        return self.es.select(label=Plant.ec)

    def add_uncont_edges(self, pair_list, **kwargs):
        return self.add_edges(pair_list, [Plant.euc] * len(pair_list), **kwargs)

    def add_cont_edges(self, pair_list, **kwargs):
        return self.add_edges(pair_list, [Plant.ec] * len(pair_list), **kwargs)

    def add_uncont_edge(self, source, target, **kwargs):
        return self.add_edge(source, target, Plant.euc, **kwargs)

    def add_cont_edge(self, source, target, **kwargs):
        return self.add_edge(source, target, Plant.ec, **kwargs)

    def unfold_to_tree(self):
        """
        Construct a tree-shaped plant with the same vertex-edge language.
        This method will not terminate for plant contain cycles
        """
        tree_plant = Plant(label_type=self.label_type)
        init_vert = self.initial_state
        cur_list = [(init_vert.index, tree_plant.add_vertex(name=init_vert["name"], label=init_vert["label"]).index)]

        names = set()
        while cur_list:
            q, qt = cur_list.pop()
            for e in self.es.select(_source=q):
                # get unique name
                name = e.target_vertex["name"]
                while name in names:
                    name = name + "'"
                names.add(name)

                qtp = tree_plant.add_vertex(name=name, label=e.target_vertex["label"]).index
                tree_plant.add_edge(qt, qtp, e["label"])
                cur_list.append((e.target, qtp))

        tree_plant.initial_state_index = self.initial_state_index

        return tree_plant

    def construct_padded(self):
        """
        Construct a plant augmented with behavior representing termination given
        by the original behavior suffixed with the termination label `PAD_VALUE`
        """
        if self.label_type is None:
            raise NotImplementedError("Padding plants with termination is only supported for plants with label types for now")
        padded_type = _construct_padded_type(self.label_type)
        # TODO - use copy instead
        padded = Plant(label_type=padded_type)
        padded.add_vertices(self.vcount(), init=self.vs["init"], label=self.vs["label"])
        padded.add_edges([(e.source, e.target) for e in self.es], [e["label"] for e in self.es])

        pad_vert = padded.add_vertex(init=False, label=PAD_VALUE).index
        padded.add_edges([(orig_vert, pad_vert) for orig_vert in padded.vs.indices],
                         [Plant.euc] * padded.vcount())
        return padded

    def self_composition(self, num_copies):
        """
        Construct an automaton representing this plant composed with itself a number of times.
        States are labeled by tuples of labels of the component states.

        Parameters
        ----------
        num_copies : int

        Returns
        -------
        SelfComposedPlant
        """

        state_attr_list = {'init', 'name', 'label'}

        def state_attr_map(*states):
            return {'init': all(v['init'] for v in states),
                    'name': tuple(v['name'] for v in states),
                    'label': tuple(v['label'] for v in states)}

        def edge_map(*edges):
            return True, ''

        init = [(self.initial_state_index,) * num_copies]
        plant_comp = SelfComposedPlant(num_copies)
        generic_sync_compose(init, state_attr_list, state_attr_map, edge_map,
                             *([self] * num_copies), dest=plant_comp)
        return plant_comp

    def sync_compose(*plants):
        """
        Compose the plants so that every plant transitions when the composition does.
        Only transitions with the same label are composed (i.e., all controllable or all uncontrollable)
        Composition states are labeled by product of each original state label type.

        Parameters
        ----------
        *plants : Iterable[Plant]
            Plants to compose

        Returns
        -------
        Plant
            The product plant
        """
        if any(plant.label_type is None for plant in plants):
            raise NotImplementedError("Synchronous composition is only supported for plants with a label type for now")
        prod_type = DataType.product_type(*[p.label_type for p in plants])

        state_attr_list = {'init', 'name', 'label'}

        if all(plant.name_type is not None for plant in plants):
            prod_name_type = DataType.product_type(*[p.name_type for p in plants])
            def state_attr_map(*states):
                return {'init': all(v["init"] for v in states),
                        'name': prod_name_type.from_subvalues(*(v["name"] for v in states)),
                        'label': prod_type.from_subvalues(*(v["label"] for v in states))}
        else:
            prod_name_type = None
            def state_attr_map(*states):
                return {'init': all(v["init"] for v in states),
                        'name': tuple(v["name"] for v in states),
                        'label': prod_type.from_subvalues(*(v["label"] for v in states))}

        def edge_map(*edges):
            return len(set(e["label"] for e in edges)) == 1, edges[0]["label"]

        init = [tuple(p.initial_state_index for p in plants)]
        gc = Plant(label_type=prod_type, name_type=prod_name_type)
        generic_sync_compose(init, state_attr_list, state_attr_map, edge_map,
                             *plants, dest=gc)
        return gc

    def alternating_compose(*plants):
        """
        Compose the plants so that one transitions when the product does, in a cycling or alternating order
        Augments the state with a counter tracking whose turn it is.

        Parameters
        ----------
        *plants : Iterable[Plant]
            The plants to compose

        Returns
        -------
        Plant
            The product
        """
        plants = list(plants)
        n = len(plants)
        if any(plant.label_type is None for plant in plants):
            raise NotImplementedError("Synchronous composition is only supported for plants with a label type for now")

        # create counter plant
        counter_name_type = DataType({"async_counter": list(range(n))})
        counter = Plant(label_type=empty_type, name_type=counter_name_type)
        counter.add_vertices(n, label=[empty_value] * n,
                             name=[counter_name_type(async_counter=i) for i in range(n)])
        counter.initial_state_index = 0
        counter.add_edges([(i, (i + 1) % n) for i in range(n)], [empty_value] * n)
        plants.append(counter)

        prod_type = DataType.product_type(*[p.label_type for p in plants])
        state_attr_list = {'init', 'name', 'label'}

        if all(plant.name_type is not None for plant in plants):
            prod_name_type = DataType.product_type(*[p.name_type for p in plants])
            def state_attr_map(*states):
                return {'init': all(v["init"] for v in states),
                        'name': prod_name_type.from_subvalues(*[s["name"] for s in states]),
                        'label': prod_type.from_subvalues(*[s["label"] for s in states])}
        else:
            prod_name_type = None
            def state_attr_map(*states):
                return {'init': all(v["init"] for v in states),
                        'name': tuple(v["name"] for v in states),
                        'label': prod_type.from_subvalues(*[s["label"] for s in states])}

        def edge_map(*edges):
            count = edges[-1].source_vertex.index
            # product transitions are formed by a counter transition and input automaton transition with same count
            is_trans = {e for e in edges if e["label"] is not None} == {edges[count], edges[-1]}
            return is_trans, edges[count]["label"]

        init = [tuple(p.initial_state_index for p in plants)]
        gc = Plant(label_type=prod_type, name_type=prod_name_type)
        generic_async_compose(init, state_attr_list, state_attr_map, edge_map,
                              *plants, dest=gc)
        return gc


class SelfComposedPlant(SingleInitialStateAutomaton):

    def __init__(self, num_copies, **kwargs):
        super().__init__(**kwargs)
        self.num_copies = num_copies



PAD_SYMBOL = "#"
PAD_TYPE = DataType({"v": [PAD_SYMBOL]})
PAD_VALUE = PAD_TYPE.default_value


def _construct_padded_type(t):
    var_value_dict = {"v": list(iter(t)) + [PAD_SYMBOL]}
    default_dict = {"v": t.default_value}
    pt = DataType(var_value_dict, default_dict)
    return pt
