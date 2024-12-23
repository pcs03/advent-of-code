from itertools import combinations

with open("./data/test23.txt") as file:
    lines = file.read().splitlines()

def add_node_to_graph(graph, node1, node2):
    try:
        graph[node1].add(node2)
    except KeyError:
        graph[node1] = set([node2])

graph: dict[str, set[str]] = {}

for line in lines:
    node1, node2 = line.split("-")

    add_node_to_graph(graph, node1, node2)
    add_node_to_graph(graph, node2, node1)

sets: set[tuple[str, str, str]] = set()

for node, edges in graph.items():
    unique_edge_combinations = list(combinations(edges, 2))

    for edge1, edge2 in unique_edge_combinations:
        if edge1 in graph[edge2]:
            pair: tuple[str, str, str] = tuple(sorted([node, edge1, edge2]))
            sets.add(pair)

count = sum(1 for combination in sets if any(node[0] == "t" for node in combination))
print(count)
