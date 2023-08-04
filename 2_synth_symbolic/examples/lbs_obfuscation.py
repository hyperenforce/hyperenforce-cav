import logging
import sys
import itertools

from time import time

from hyper_synth.automata import Plant
from hyper_synth.datatype import DataType
from hyper_synth.qbf_encoding import ControllerSynthesisEncodingQBF
from hyper_synth.qbf_solver import QBFSolver
from obfuscation.obfuscation_plant import create_obfuscation_plant_and_spec
from obfuscation.obfuscation_spec import *
from obfuscation.obfuscation_spec_symbolic import *


def map_plant(width, height, unfold_to_tree=False, remove_bad_inf=True,
              cs_opacity=True, source_as_inf=True, num_keys=2, sec_regs=None):
    """
    This constructs the plant where the source output, network/obfuscator output, and inferred output are all a single bit.
    """
    rows = list(range(height))
    cols = list(range(width))
    indices = list(range(width * height))
    coords2ind = {(r, c): r * width + c for r in rows for c in cols}
    ind2row = {v: k[0] for k, v in coords2ind.items()}
    ind2col = {v: k[1] for k, v in coords2ind.items()}

    if sec_regs is None:
        sec_regs = []
    source_type = DataType({"row": rows, "col": cols, "sec": list(itertools.product(*([[False, True]]*len(sec_regs))))})
    source = Plant(label_type=source_type)

    source.add_vertices(width * height, label=[source_type(row=ind2row[i], col=ind2col[i],
                                                           sec=(tuple((ind2row[i], ind2col[i]) in reg for reg in sec_regs))) for i in indices])
    #source.initial_state_index = 0
    source.initial_state_index = indices[-1]
    source.add_uncont_edges([(coords2ind[(r, c)], coords2ind[(r+1, c)]) for r in rows[:-1] for c in cols])
    source.add_uncont_edges([(coords2ind[(r, c)], coords2ind[(r, c+1)]) for r in rows for c in cols[:-1]])
    source.add_uncont_edge(indices[-1], 0)

    source.vs["name"] = source.vs["label"]
    source.name_type = source.label_type

    sec_out = {"sec"}
    #inf_out = {"sec"}
    inf_out = {"row", "col"}
    obs_out = {"row", "col"}

    net_names = {"row": "net_r", "col": "net_c", "sec": "net_sec"}
    #inf_names = {"sec": "inf_sec"}
    inf_names = {"row": "inf_r", "col":"inf_col"}

    plant, type_dict, spec_dict, plant_state_encoding, label_encoding, label_func\
        = create_obfuscation_plant_and_spec(source, sec_out, inf_out, obs_out,
                                            net_names=net_names, inf_names=inf_names,
                                            remove_bad_inf=remove_bad_inf,
                                            cs_opacity=cs_opacity, source_as_inf=source_as_inf,
                                            num_keys=num_keys)

    if unfold_to_tree:
        plant = plant.unfold_to_tree()
    return plant, type_dict, inf_names, plant_state_encoding, label_encoding, label_func

def log_auto_info(logger, name, automaton):
    msg = f"{name} info - "+\
          f"Vertices: {automaton.vcount()} "+\
          f"Edges: {automaton.ecount()}"
    logger.info(msg)

def log_time(logger, name, last):
    cur_time = time()
    logger.info(f"{name} time(s): {cur_time - last}")
    return cur_time


def run_obfuscation_synthesis_qbf_symbolic():
    cs_opacity = False
    source_as_inf = True
    height = 3
    width = 2
    num_keys = 2

    logger = logging.getLogger(__name__)
    logger.info(f"Map height: {height}, width: {width}")
    logger.info(f"Number of keys: {num_keys}")

    start = time()
    plant, type_dict, inf_names,\
    plant_state_encoding, label_encoding, label_func = map_plant(width, height, cs_opacity=cs_opacity,
                                                                 source_as_inf=source_as_inf,
                                                                 num_keys=num_keys,
                                                                 sec_regs=[ {(2,0)}])
    log_auto_info(logger, "Plant", plant)

    h_priv = privacy_sybmolic_hyperautomaton(type_dict, label_encoding, cs_opacity=cs_opacity)
    log_auto_info(logger, "Privacy hyperautomaton", h_priv)
    h_pipe_1 = pipeline_1_sybmolic_hyper_auto(type_dict, label_encoding)
    log_auto_info(logger, "Dependency hyperautomaton 1", h_pipe_1)
    h_pipe_2 = pipeline_2_sybmolic_hyper_auto(type_dict, label_encoding, alternate=source_as_inf)
    log_auto_info(logger, "Dependency hyperautomaton 2", h_pipe_2)

    start = log_time(logger, "Model setup", start)

    solver = QBFSolver(verbose=False, num_threads=8)
    # TODO - test all specifications
    prob = ControllerSynthesisEncodingQBF(plant, h_priv, h_pipe_1, h_pipe_2,
                                          plant_state_enc=plant_state_encoding,
                                          label_enc=label_encoding,
                                          label_func=label_func,
                                          quantify_path_steps=False,
                                          solver=solver,
                                          max_depth=(2 * (width + height - 1)))
    prob.encode()
    start = log_time(logger, "Encoding to QBF", start)

    output = prob.solve()
    start = log_time(logger, "Solving QBF", start)

    controller = prob.decode_controller(output.model)
    start = log_time(logger, "Extracting controller", start)

    log_auto_info(logger, "Controller", controller)

    #print(controller)

    time()
    assert controller

    return controller


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                        format= '[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
                        datefmt='%H:%M:%S')
    run_obfuscation_synthesis_qbf_symbolic()
