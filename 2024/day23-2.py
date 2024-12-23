from itertools import combinations

with open("./data/day23.txt") as file:
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

def is_connected(comb: list[str]) -> bool:
    for i in range(len(comb)):
        for j in range(len(comb)):
            if i == j:
                continue
            
            if comb[i] not in graph[comb[j]]:
                return False

    return True


sets: set[tuple[str, ...]] = set()

for node, edges in graph.items():
    unique_combinations: set[tuple[str, ...]] = set()

    for r in range(1, len(edges) + 1):
        new_combinations: set[tuple[str, ...]] = set(combinations(edges, r))
        unique_combinations = unique_combinations.union(new_combinations)

    for comb in unique_combinations:
        comb = list(comb)

        if is_connected(comb):
            sets.add(tuple(sorted([node , *comb])))

max = 0
max_set: tuple[str, ...] | None = None

for s in sets:
    if len(s) > max:
        max = len(s)
        max_set = s

print(max, max_set)

if max_set is None:
    raise RuntimeError("No max set found")

print(','.join(max_set))
