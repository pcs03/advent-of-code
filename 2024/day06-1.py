with open("./data/day06.txt", "r") as file:
    grid = [list(line) for line in file.read().splitlines()]

def find_guard() -> tuple[int, int]:
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char not in ['#', '.']:
                return (i, j)
    raise RuntimeError("No guard found")

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

def trace_path():
    visited: set[tuple[int, int]] = set()
    position = find_guard()
    direction = 0

    while True:
        visited.add(position)
        delta = directions[direction]

        new_position = position[0] + delta[0], position[1] + delta[1]

        if new_position[0] < 0 or new_position[0] >= len(grid) or new_position[1] < 0 or new_position[1] >= len(grid[0]):
            break

        new_position_char = grid[new_position[0]][new_position[1]]
        print(position, new_position_char)

        while new_position_char == '#':
            direction = (direction + 1) % 4
            delta = directions[direction]
            new_position = position[0] + delta[0], position[1] + delta[1]
            new_position_char = grid[new_position[0]][new_position[1]]

        position = new_position 

    return len(visited)


print(trace_path())

