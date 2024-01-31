with open("./data/test23.txt", "r") as file:
    grid = file.read().splitlines()

goal = (22, 21)

slopes = {
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0),
    "^": (-1, 0),
}

class Node():
    def __init__(self, state, cost, parent):
        self.state = state
        self.cost = cost
        self.parent = parent
        self.char = grid[self.state[0]][self.state[1]]

    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __repr__(self):
        return f"{self.state}, with {self.cost}"

    def print_grid(self):
        g = [list(row) for row in grid.copy()]

        node = self
        while node:
            g[node.state[0]][node.state[1]] = "O"
            node = node.parent
        return [f"{i:02} " + "".join(row) for i, row in enumerate(g)]




start = Node((0, 1), 0, None)

def dfs(start: Node, visited = set()):
    visited.add(start.state)
    print(start)

    if start.state == goal:
        print(start.state, start.cost, start.char)
        for row in start.print_grid():
            print(row)
        return start.cost

    neighbours = []

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    if start.char in slopes:
        directions = [slopes[start.char]]

    for dir in directions:
        n = (start.state[0] + dir[0], start.state[1] + dir[1])
        if n[0] < 0 or n[0] >= len(grid) or n[1] < 0 or n[1] >= len(grid[0]):
            continue
        char = grid[n[0]][n[1]] 

        if char == "#":
            continue

        if n in visited:
            continue

        neighbours.append(Node(n, start.cost + 1, start))
    print(neighbours)
    costs = []

    for n in neighbours:
        costs.append(dfs(n, visited))

    if not costs:
        return 0

    return max(costs)



print(dfs(start)) 
