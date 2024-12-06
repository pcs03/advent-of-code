with open("./data/day06.txt", "r") as file:
    grid = [list(line) for line in file.read().splitlines()]

def find_guard() -> tuple[int, int]:
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char not in ['#', '.']:
                return (i, j)
    raise RuntimeError("No guard found")

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
starting_position = find_guard()

def trace_path(limit: int = 10000):
    visited: set[tuple[int, int]] = set()
    position = starting_position
    direction = 0

    steps = 0

    while True:
        visited.add(position)
        delta = directions[direction]

        new_position = position[0] + delta[0], position[1] + delta[1]

        if new_position[0] < 0 or new_position[0] >= len(grid) or new_position[1] < 0 or new_position[1] >= len(grid[0]):
            break

        new_position_char = grid[new_position[0]][new_position[1]]

        while new_position_char == '#':
            direction = (direction + 1) % 4
            delta = directions[direction]
            new_position = position[0] + delta[0], position[1] + delta[1]
            new_position_char = grid[new_position[0]][new_position[1]]


        position = new_position 
        steps += 1

        if steps > limit:
            return True

    return False


sum = 0
for col in range(len(grid)):
    for row in range(len(grid)):
        char = grid[col][row]
        if char == "#":
            continue

        if (col, row) == starting_position:
            continue

        grid[col][row] = "#"
        result = trace_path()
        grid[col][row] = "."

        if result:
            sum += 1


print(sum)
