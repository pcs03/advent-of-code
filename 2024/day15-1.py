with open("./data/test15-1.txt") as file:
    grid, moves = file.read().split("\n\n")

    grid = [list(line) for line in grid.splitlines()]
    moves = moves.strip().replace("\n", "")

number_rows = len(grid)
number_cols = len(grid[0])

directions = {
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
    "^": (-1, 0),
}

def find_robot():
    for row in range(number_rows):
        for col in range(number_cols):
            if grid[row][col] == "@":
                return (row, col)
    raise ValueError("No robot found.")

pos = find_robot()
grid[pos[0]][pos[1]] = "."

for move in moves:
    dir = directions[move]
    steps = 1

    chars: list[tuple[str, tuple[int, int]]] = []
    while True:

        new_pos = pos[0] + steps * dir[0], pos[1] + steps * dir[1]
        char = grid[new_pos[0]][new_pos[1]]

        if char == "#":
            break
        chars.append((char, new_pos))
        steps += 1

    print(chars)

    if len(chars) == 0:
        continue

    if len(chars) == 1:
        if chars[0][0] == ".":
            pos = chars[0][1]
            continue
        else:
            continue

    indices = []

    for char, charpos in chars:
        if char






print(grid)
print(moves)
