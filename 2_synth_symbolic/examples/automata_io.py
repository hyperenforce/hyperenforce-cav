import os

from hyper_synth.automata import HyperAutomaton, Plant
from tests.test_hyperauto import hyper_auto_ex1, plant_ex1

example_files_dir = os.path.abspath(os.path.dirname(__file__))


def example_writing():
    p = plant_ex1()

    # Visualize in Browser or edit in program like Inkscape
    p.write_svg(os.path.join(example_files_dir, "ex.svg"), to_inkscape=False)

    # Visualize using graphviz
    # Online interface available at: https://dreampuf.github.io/GraphvizOnline/
    p.write_dot_f(os.path.join(example_files_dir, "ex.dot"))


if __name__ == "__main__":
    example_writing()
