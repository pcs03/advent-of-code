with open("./data/test12.txt") as file:
    grid = [list(line) for line in file.read().splitlines()]

print(grid)

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def get_options(direction: int) -> list[tuple[int, tuple[int, int]]]:
    opts = [(direction + i - 1) % 4 for i in range(4)]
    return [(d, DIRS[d]) for d in opts]

def walk_perimeter(pos: tuple[int, int]) -> list[tuple[int, int]]:
    start = pos
    char = grid[pos[0]][pos[1]]
    dir = 0

    corners = [start]

    while True:
        for new_dir, delta in get_options(dir):
            # print("OPT", new_dir, delta)

            new_pos = (pos[0] + delta[0], pos[1] + delta[1])
            new_char = grid[new_pos[0]][new_pos[1]]

            if new_char == char:
                if new_dir != dir:
                    corners.append((pos))
                    dir = new_dir
                pos = new_pos
                break

        if pos == start:
            if len(corners) != 0:
                corners.append(start)
            break

    return corners

def get_perimeter(corners: list[tuple[int, int]]) -> int:
    length = 0

    for i in range(0, len(corners)  - 1):
        pos1 = corners[i]
        pos2 = corners[i + 1]

        dr = pos2[0] - pos1[0]
        dc = pos2[1] - pos1[1]

        delta_length = abs(dr) + abs(dc)
        print(pos1, pos2, delta_length)

        length += delta_length

    return length



# BUG: FUCK THIS FUCKING BULLSHIT

corners = walk_perimeter((0, 0))
print(corners)
print(get_perimeter(corners))

