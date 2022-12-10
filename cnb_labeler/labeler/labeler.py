from cnb_labeler.def_graph.create_graph import create_graph
from config import LABELS

from argparse import ArgumentParser
import os
import json

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("degree", type=int)
    parser.add_argument("filename", type=str)
    args = parser.parse_args()
    return args.degree, args.filename


def create_label(graph):



def main():
    degree, filename = parse_args()
    dir_path = os.path.join(LABELS, str(degree))

    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    
    graph = create_graph()
    labels = []