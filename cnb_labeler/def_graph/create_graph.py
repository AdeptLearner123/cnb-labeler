import networkx as nx

from config import DEF_EDGES, SEM_LINK_EDGES

def add_relation(graph, sense1, sense2, relation_type, relation_data):
    graph.add_edge(sense1, sense2)

    if "relations" not in graph[sense1][sense2]:
        graph[sense1][sense2]["relations"] = []
    graph[sense1][sense2]["relations"].append((relation_type, relation_data))


def create_graph():
    graph = nx.DiGraph()

    with open(DEF_EDGES, "r") as file:
        lines = file.read().splitlines()
        for line in lines:
            (sense1, sense2, sentence_id, start_idx, end_idx) = line.split("\t")
            add_relation(graph, sense1, sense2, "TEXT", (sentence_id, start_idx, end_idx))
    
    with open(SEM_LINK_EDGES, "r") as file:
        lines = file.read().splitlines()
        for line in lines:
            (sense1, sense2, sem_link) = line.split("\t")
            add_relation(graph, sense1, sense2, "SEM_LINK", sem_link)

    return graph