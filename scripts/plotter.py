import argparse
import math
import os
import sys
from typing import List, Tuple
from itertools import product
import matplotlib.pyplot as plt

from py_factor_graph.utils.logging_utils import logger
from py_factor_graph.factor_graph import FactorGraphData

FONT_SIZE = 10
DPI = 1200

def rbcd_plot(args) -> None:
    dataset = args.dataset
    output_dir = args.output_dir
    f_sdp = args.f_sdp

    iter = []
    robot = []
    norm_cost = []
    gradnorm = []

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    logger.info(f"Plotting RBCD output from {dataset} to {output_dir}")

    # Parse RBCD output
    with open(dataset, "r") as f:
        for line in f:
            if not line.startswith("#"): # Skip comments
                iter.append(int(line.split()[0]))
                robot.append(int(line.split()[1]))
                gradnorm.append(float(line.split()[3]))

                # Normalize cost
                cost = float(line.split()[2])
                norm_cost.append((cost - f_sdp) / f_sdp)
    
    # Plot iterations vs. normalized cost
    plt.figure()
    plt.rcParams['figure.facecolor'] = 'white'
    # plt.gca().set_aspect('equal')
    plt.plot(iter, norm_cost)
    plt.xlabel("Iteration", fontsize=FONT_SIZE)
    plt.ylabel("Normalized Cost", fontsize=FONT_SIZE)
    plt.title("Iterations vs. Normalized Cost", fontsize=FONT_SIZE)
    plt.grid(True, color='gray')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "iter_vs_cost.png"), dpi=DPI)

    # Plot iterations vs. gradnorm
    plt.figure()
    plt.rcParams['figure.facecolor'] = 'white'
    # plt.gca().set_aspect('equal')
    plt.plot(iter, gradnorm)
    plt.xlabel("Iteration", fontsize=FONT_SIZE)
    plt.ylabel("Gradnorm", fontsize=FONT_SIZE)
    plt.title("Iterations vs. Gradnorm", fontsize=FONT_SIZE)
    plt.grid(True, color='gray')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "iter_vs_gradnorm.png"), dpi=DPI)
    


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
    parser.add_argument(
        "-f",
        "--f_sdp",
        type=float,
        default=1.0,
        help="scaling factor for the SDP cost",
    )

    args = parser.parse_args()
    rbcd_plot(args)

if __name__ == "__main__":
    main(sys.argv[1:])