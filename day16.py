import time

with open("./data/day16.txt", "r") as file:
    lines = file.read().splitlines()


def bfs(start):
    visited = set([(start.state, start.direction)])
    states = set([start.state])

    queue = [start]

    while queue:
        node = queue.pop(0)

        neighbours = node.neighbours()

        for n in neighbours:
            if (n.state, n.action) not in visited:
                visited.add((n.state, n.action))
                states.add(n.state)
                queue.append(n)
    return len(states)


class Node:
    options = {
        ".": {
            (1, 0): [(1, 0)],
            (-1, 0): [(-1, 0)],
            (0, 1): [(0, 1)],
            (0, -1): [(0, -1)],
        },
        "/": {
            (1, 0): [(0, -1)],
            (-1, 0): [(0, 1)],
            (0, 1): [(-1, 0)],
            (0, -1): [(1, 0)],
        },
        "\\": {
            (1, 0): [(0, 1)],
            (-1, 0): [(0, -1)],
            (0, 1): [(1, 0)],
            (0, -1): [(-1, 0)],
        },
        "|": {
            (1, 0): [(1, 0)],
            (-1, 0): [(-1, 0)],
            (0, 1): [(-1, 0), (1, 0)],
            (0, -1): [(-1, 0), (1, 0)],
        },
        "-": {
            (1, 0): [(0, 1), (0, -1)],
            (-1, 0): [(0, 1), (0, -1)],
            (0, 1): [(0, 1)],
            (0, -1): [(0, -1)],
        },
    }

    def __init__(self, state, action, direction=None):
        self.direction = direction
        self.state = state
        self.action = action

    def neighbours(self):
        if self.direction is None:
            self.direction = (
                self.state[0] - self.action[0],
                self.state[1] - self.action[1],
            )
        char = lines[self.state[0]][self.state[1]]

        directions = self.options[char][self.direction]
        neighbours = [(self.state[0] + dir[0], self.state[1] + dir[1])
                      for dir in directions]

        return [
            Node(n, self.state)
            for n in neighbours
            if n[0] >= 0 and n[1] >= 0 and n[0] < len(lines[0]) and n[1] < len(lines[0])
        ]

    def __repr__(self):
        return f"S: {self.state}, A: {self.action}"


def generate_start_nodes():
    starts = []

    for i in range(len(lines)):
        starts.append(Node((i, 0), None, (0, 1)))
        starts.append(Node((i, len(lines[0]) - 1), None, (0, -1)))

    for i in range(len(lines[0])):
        starts.append(Node((0, i), None, (1, 0)))
        starts.append(Node((len(lines) - 1, i), None, (-1, 0)))

    return starts


def main():
    starttime = time.time()
    highest_num = 0
    highest_node = None

    starts = generate_start_nodes()

    for start in starts:
        num = bfs(start)
        if num > highest_num:
            highest_num = num
            highest_node = start

    print(highest_num)
    print(highest_node)
    print(f"Time: {time.time() - starttime}")


if __name__ == "__main__":
    main()
