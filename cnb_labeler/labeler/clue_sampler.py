import random

from cnb_labeler.utils.get_bridge_edges import get_bridge_edges


def sample_clue(graph, degree):
    source_sense, target_sense = sample_sense_pair(graph, degree)
    bridge_edges = get_bridge_edges(graph, source_sense, target_sense, degree)
    return source_sense, target_sense, bridge_edges


def sample_sense_pair(graph, degree):
    source = random.choice(list(graph.nodes))
    explored = set([ source ])

    current = source
    out_only = False
    for _ in range(degree):
        predecessors = graph.predecessors(current)
        successors = graph.successors(current)

        if out_only:
            neighbors = predecessors
        else:
            neighbors = predecessors + successors

        neighbors = [ neighbor for neighbor in neighbors if neighbor not in explored ]
        current = random.choice(neighbors)
        explored.update(neighbors)
        out_only = current in predecessors
    
    return source, current
