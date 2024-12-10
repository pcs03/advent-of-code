with open("./data/day10.txt") as file:
    grid = [list(map(int, list(row))) for row in file.read().splitlines()]


total_columns = len(grid)
total_rows = len(grid[0])

starting_positions: set[tuple[int, int]] = set()

for col in range(total_columns):
    for row in range(total_rows):
        char = grid[col][row]
        if char == 0:
            starting_positions.add((col, row))

def find_trails(pos: tuple[int, int], number: int = 0) -> int:
    if number == 9:
        return 1

    valid_paths = 0

    for edge in (
        (pos[0] + 1, pos[1]),
        (pos[0] - 1, pos[1]),
        (pos[0], pos[1] + 1),
        (pos[0], pos[1] - 1),
    ):
        if edge[0] < 0 or edge[0] >= total_columns or edge[1] < 0 or edge[1] >= total_rows:
            continue
        
        number_at_edge = grid[edge[0]][edge[1]]
        if number_at_edge == number + 1:
            valid_paths += find_trails(edge, number + 1)

    return valid_paths

sum = 0
for pos in starting_positions:
    trails = find_trails(pos)
    sum += trails

print(sum)


