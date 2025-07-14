from __future__ import annotations

with open("./data/test20.txt") as file:
    grid = [list(line) for line in file.read().splitlines()]

number_rows = len(grid)
number_cols = len(grid[0])

start, end = None, None
for row in range(number_rows):
    for col in range(number_cols):
        char = grid[row][col]
        if char == "S":
            start = (row, col)
        if char == "E":
            end = (row, col)

if start is None or end is None:
    raise ValueError("start or end is not found")


class Node:
    def __init__(self, pos: tuple[int, int], parent: Node | None, distance: int):
        self.pos: tuple[int, int] = pos
        self.parent: Node | None = parent
        self.distance: int = distance

    def backtrace(self) -> set[tuple[int, int]]:
        node = self
        route: set[tuple[int, int]] = set()

        while node.parent is not None:
            print(node.pos)
            route.add(node.pos)
            node = node.parent

        return route


def dfs(node: Node, visited: set[tuple[int, int]], cheat: int) -> set[int]:
    visited.add(node.pos)

    pos = node.pos
    # print(node.pos, node.distance)
    if pos == end:
        return set([node.distance])

    # for r in range(number_rows):
    #     for c in range(number_cols):
    #         if (r,c) in visited:
    #             print("o", end="")
    #         else:
    #             print(grid[r][c], end="")
    #
    #     print()

    results: set[int] = set()

    for edge in [
        (pos[0] + 1, pos[1]),
        (pos[0] - 1, pos[1]),
        (pos[0], pos[1] + 1),
        (pos[0], pos[1] - 1),
    ]:
        if edge in visited:
            continue
        if edge[0] < 0 or edge[0] >= number_rows or edge[1] < 0 or edge[1] >= number_cols:
            continue

        char = grid[edge[0]][edge[1]]
        if char == "#":
            if not (node.distance == cheat or node.distance == cheat + 1) :
                continue

        results.update(dfs(Node(edge, node, node.distance + 1), visited.copy(), cheat))
    return results


base = dfs(Node(start, None, 0), set(), -10).pop()

cheats: dict[int, int] = {}

for i in range(base):
    res = dfs(Node(start, None, 0), set(), i)
    valid_cheats = [num for num in list(res) if num < base]
    print(valid_cheats)

    for cheat in valid_cheats:
        try:
            cheats[cheat] += 1
        except KeyError:
            cheats[cheat] = 1


print(cheats)
