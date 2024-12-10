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

def find_trails(pos: tuple[int, int]) -> int:
    nines: set[tuple[int, int]] = set()

    queue: list[tuple[int, int]] = []

    queue.append(pos)

    while not len(queue) == 0:
        pos = queue.pop(0)
        for edge in (
            (pos[0] + 1, pos[1]),
            (pos[0] - 1, pos[1]),
            (pos[0], pos[1] + 1),
            (pos[0], pos[1] - 1),
        ):
            if edge[0] < 0 or edge[0] >= total_columns or edge[1] < 0 or edge[1] >= total_rows:
                continue
            
            current_number = grid[pos[0]][pos[1]]
            number_at_edge = grid[edge[0]][edge[1]]
            if number_at_edge == current_number + 1:
                if number_at_edge == 9:
                    nines.add(edge)
                else:
                    queue.append(edge)

    return len(nines)



sum = 0
for pos in starting_positions:
    trails = find_trails(pos)
    sum += trails

print(sum)

