from __future__ import annotations
import heapq

with open("./data/day16.txt") as file:
    grid = [list(line) for line in file.read().splitlines()]

print(grid)

number_rows = len(grid)
number_cols = len(grid[0])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Node:
    def __init__(self, pos: tuple[int, int], parent: Node | None, direction: int, distance: int):
        self.pos: tuple[int, int] = pos
        self.parent: Node | None = parent
        self.distance: int = distance
        self.direction: int = direction

    def __lt__(self, other: Node):
        return self.distance < other.distance

    def __le__(self, other: Node):
        return self.distance <= other.distance

    def __gt__(self, other: Node):
        return self.distance > other.distance

    def __ge__(self, other: Node):
        return self.distance >= other.distance

    def __repr__(self) -> str:
        return f"Node with position {self.pos}, distance {self.distance}"

    def backtrace(self) -> set[tuple[int, int]]:
        print(f"Backtracing from {self.pos} at {self.distance}")
        path: set[tuple[int, int]] = set([self.pos])

        node = self.parent
        while node is not None:
            print(f"{node.pos} at {node.distance}")
            path.add(node.pos)
            node = node.parent

        return path

    def get_neighbours(self, visited: set[tuple[int, int]]) -> list[Node]:
        neighbours: list[Node] = []

        for dir_number in [
            self.direction,
            (self.direction - 1) % 4,
            (self.direction + 1) % 4,
        ]:
            direction = directions[dir_number]
            edge = self.pos[0] + direction[0], self.pos[1] + direction[1]

            if edge[0] < 0 or edge[0] >= number_rows or edge[1] < 0 or edge[1] >= number_cols:
                continue

            if edge in visited:
                continue

            char = grid[edge[0]][edge[1]]

            if char == "#":
                continue

            added_distance = 0
            if dir_number == self.direction:
                added_distance = 1
            else:
                added_distance = 1001

            node = Node(edge, self, dir_number, self.distance + added_distance)

            neighbours.append(node)

        return neighbours


def get_start_end_locations():
    start, end = None, None

    for row in range(number_rows):
        for col in range(number_cols):
            char = grid[row][col]
            if char == "S":
                start = (row, col)
            if char == "E":
                end = (row, col)

    if start is None or end is None:
        raise ValueError("No start or end")

    return start, end


start_pos, end_pos = get_start_end_locations()
start = Node(start_pos, None, 1, 0)

pq: list[Node] = [start]
visited: set[tuple[int, int]] = set()

minimum_path = None
path_tiles: set[tuple[int, int]] = set()

while len(pq) > 0:
    node = heapq.heappop(pq)

    if node.pos == end_pos:
        path = node.backtrace()
        print(f"Found goal {node.pos} at distance {node.distance}")
        print(len(path))

        if minimum_path is not None:
            if len(path) == minimum_path:
                path_tiles = path_tiles.union(path)
        else:
            minimum_path = len(path)
            path_tiles.union(path)


    for edge in node.get_neighbours(visited):
        heapq.heappush(pq, edge)
        # edge = Node(edge_pos, node, )
    visited.add(node.pos)

print(minimum_path)
