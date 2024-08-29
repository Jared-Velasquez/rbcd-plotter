import argparse
import math
import os
import sys
from typing import List, Tuple
from itertools import product
import matplotlib.pyplot as plt

from py_factor_graph.utils.logging_utils import logger
from py_factor_graph.factor_graph import FactorGraphData

def rbcd_plot(args) -> None:
    pass

def main(args):
    parser = argparse.ArgumentParser(
        description="This script is used to visualize normalized cost and gradnorm of the Riemannian Block Coordinate Descent optimization method"
    )
    parser.add_argument(
        "-d",
        "--dataset",
        type=str,
        required=True,
        help="filepath of RBCD output",
    )
    parser.add_argument(
        "-o",
        "--output_dir",
        type=str,
        required=True,
        help="directory where results are saved",
    )

    args = parser.parse_args()
    rbcd_plot(args)

if __name__ == "__main__":
    main(sys.argv[1:])