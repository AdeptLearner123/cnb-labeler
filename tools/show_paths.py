from cnb_labeler.utils.get_bridge_edges import get_bridge_edges
from cnb_labeler.def_graph.create_graph import create_graph
from config import DICTIONARY

import networkx as nx
import matplotlib.pyplot as plt
from argparse import ArgumentParser
import json
from collections import defaultdict

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("source_sense", type=str)
    parser.add_argument("target_sense", type=str)
    parser.add_argument("degree", type=int)
    args = parser.parse_args()
    return args.source_sense, args.target_sense, args.degree


def main():
    source_sense, target_sense, degree = parse_args()

    print("Status", "Creating graph")
    graph = create_graph()
    
    print("Status", "Reading dictionary")
    with open(DICTIONARY, "r") as file:
        dictionary = json.loads(file.read())

    print("Status", "Getting bridge edges")
    bridge_edges = get_bridge_edges(graph, source_sense, target_sense, degree)
    print(bridge_edges)
    print("Total bridge edges", len(bridge_edges))

    edge_labels = defaultdict(lambda: [])
    node_labels = dict()

    subgraph = nx.DiGraph()

    for sense1, sense2, relation_type, relation_data in bridge_edges:
        subgraph.add_edge(sense1, sense2)
        
        if sense1 not in node_labels:
            node_labels[sense1] = dictionary[sense1]["word"]
        if sense2 not in node_labels:
            node_labels[sense2] = dictionary[sense2]["word"]
        
        edge_labels[(sense1, sense2)].append(relation_type)
    print(subgraph.edges)

    edge_labels = { edge_key: ",".join(relations) for edge_key, relations in edge_labels.items() }
    print(edge_labels)
    print(node_labels)

    pos = nx.spring_layout(subgraph)
    nx.draw_networkx(subgraph, pos=pos, labels=node_labels, with_labels = True)
    nx.draw_networkx_edge_labels(subgraph, edge_labels=edge_labels, pos=pos)
    plt.show()