from cnb_labeler.def_graph.create_graph import create_graph
from cnb_labeler.utils.print_edge import print_edge
from .clue_sampler import sample_clue
from config import LABELS, SENTENCES, DICTIONARY

from argparse import ArgumentParser
import os
import json

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("degree", type=int)
    parser.add_argument("filename", type=str)
    args = parser.parse_args()
    return args.degree, args.filename


def create_label(graph, degree, dictionary, sentence_dict):
    source_sense, target_sense, bridge_edges = sample_clue(graph, degree)
    print(dictionary[source_sense]["word"])
    print(dictionary[target_sense]["word"])

    for sense1, sense2, relation_type, relation_data in bridge_edges:
        print_edge(sense1, sense2, relation_type, relation_data, dictionary, sentence_dict)

    clue_label = input("[0 = Unrelated, 1=Related, 2=Weak clue, 3=Anticlue, 4=Bad disambiguation] : ")

    if len(clue_label) == 0:
        return None

    return {
        "source_sense": source_sense,
        "source_word": dictionary[source_sense]["word"],
        "target_sense": target_sense,
        "target_word": dictionary[target_sense]["word"],
        "subgraph": bridge_edges,
        "label": int(clue_label)
    }


def main():
    degree, filename = parse_args()
    dir_path = os.path.join(LABELS, str(degree))

    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    print("Status", "Creating graph")
    graph = create_graph()

    with open(DICTIONARY, "r") as file:
        dictionary = json.loads(file.read())
    
    with open(SENTENCES, "r") as file:
        sentence_dict = json.loads(file.read())

    labels = []
    file_path = os.path.join(dir_path, f"{filename}.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            labels = json.loads(file.read())

    while(True):
        new_label = create_label(graph, degree, dictionary, sentence_dict)

        if new_label is None:
            break

        labels.append(new_label)

        with open(file_path, "w+") as file:
            file.write(json.dumps(labels, indent=4, ensure_ascii=False))