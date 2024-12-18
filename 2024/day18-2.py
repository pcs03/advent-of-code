from __future__ import annotations

grid_size = 71

with open("./data/day18.txt") as file:
    positions: list[tuple[int, int]] = [tuple(map(int, line.split(","))) for line in file.read().splitlines()]

class Node:
    def __init__(self, pos: tuple[int, int], parent: Node | None, distance: int):
        self.pos: tuple[int, int] = pos
        self.parent: Node | None = parent
        self.distance: int = distance

    def backtrace(self) -> set[tuple[int, int]]:
        node = self
        route: set[tuple[int, int]] = set()

        while node.parent is not None:
            route.add(node.pos)
            node = node.parent

        return route


def bfs(start: tuple[int, int], end: tuple[int, int], positions: list[tuple[int, int]]) -> int:
    visited: set[tuple[int, int]] = set([start])
    q: list[Node] = [Node(start, None, 0)]

    while len(q) > 0:
        node = q.pop(0)
        pos = node.pos

        if pos == end:
            return node.distance

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

            q.append(Node(edge, node, node.distance + 1))
            visited.add(edge)

    return -1

def binary_search(minimum_bytes: int, maximum_bytes: int) -> tuple[int, int]:
    left = minimum_bytes
    right = maximum_bytes
    result = -1

    while left <= right:
        mid = (left + right) // 2
        short_positions: list[tuple[int, int]] = positions[:mid]
        path_len = bfs((0, 0), (grid_size - 1, grid_size - 1), short_positions)

        if path_len == -1:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return positions[result - 1]

result = binary_search(1024, len(positions) - 1)

print(result)
