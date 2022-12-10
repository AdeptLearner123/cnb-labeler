from collections import defaultdict

def get_successor_edges(graph, node, degree):
    queue = [ node ]
    explored = set([ node ])
    path_edges = defaultdict(lambda: [])
    path_lengths = { node: 0 }

    while len(queue) > 0:
        current = queue.pop(0)
        current_degree = path_lengths[current]

        successors = graph.successors(current)
        successors = [ successor for successor in successors if successor not in explored ]
        explored.update(successors)

        for successor in successors:
            relations = graph[current][successor]["relations"]
            edges = [ (current, successor, relation_type, relation_data) for relation_type, relation_data in relations ]
            path_edges[successor] += edges + path_edges[current]
            path_lengths[successor] = current_degree + 1
        
        if current_degree < degree:
            queue += successors
    
    return path_edges, path_lengths



def get_bridge_edges(graph, source, target, degree):
    source_path_edges, source_path_lengths = get_successor_edges(graph, source, degree)
    target_path_edges, target_path_lengths = get_successor_edges(graph, target, degree)
    bridge_nodes = set(source_path_edges.keys()).intersection(set(target_path_edges.keys()))
    bridge_edges = defaultdict(lambda: [])

    for node in bridge_nodes:
        path_length = source_path_lengths[node] + target_path_lengths[node]
        bridge_edges[path_length] += source_path_edges[node] + target_path_edges[node]
    
    min_length = min(bridge_edges.keys())
    return bridge_edges[min_length]