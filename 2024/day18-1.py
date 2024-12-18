from __future__ import annotations

grid_size = 71
num_bytes = 1024

with open("./data/day18.txt") as file:
    positions = [tuple(map(int, line.split(","))) for line in file.read().splitlines()]

positions = positions[:num_bytes]


class Node:
    def __init__(self, pos: tuple[int, int], parent: Node | None):
        self.pos: tuple[int, int] = pos
        self.parent: Node | None = parent

    def backtrace(self) -> set[tuple[int, int]]:
        node = self
        route: set[tuple[int, int]] = set()

        while node.parent is not None:
            route.add(node.pos)
            node = node.parent

        return route


grid: list[list[str]] = []

start = (0, 0)
end = (grid_size - 1, grid_size - 1)

visited: set[tuple[int, int]] = set([start])
q: list[Node] = [Node(start, None)]

while len(q) > 0:
    node = q.pop(0)
    pos = node.pos

    if pos == end:
        print(f"Found {node.pos}")
        route = node.backtrace()
        print(len(route))
        break

    for edge in [
        (pos[0] + 1, pos[1]),
        (pos[0] - 1, pos[1]),
        (pos[0], pos[1] + 1),
        (pos[0], pos[1] - 1),
    ]:
        if edge[0] < 0 or edge[0] >= grid_size or edge[1] < 0 or edge[1] >= grid_size:
            continue

        if edge in visited:
            continue

        if edge in positions:
            continue

        q.append(Node(edge, node))
        visited.add(edge)
