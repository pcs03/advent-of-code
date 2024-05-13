# yeah the code is messy I know, and inefficient, but it works lol
# To calculate whether a tile is inside or outside the loop, it uses the following:
# For every non-loop point, the amount of path collosions are calculated to the outside
# If it crosses an odd number of times, it's inside the loop. Even, means it's outside of the loop
# A nice visualization is created when run

with open("./data/day10.txt", "r") as file:
    lines = file.read().splitlines()

dir_map = {
    "|": [0, 2],
    "-": [3, 1],
    "L": [0, 1],
    "J": [0, 3],
    "7": [2, 3],
    "F": [2, 1],
    ".": [],
}
s_idx = None
for i, line in enumerate(lines):
    if "S" in line:
        row_idx = line.find("S")
        s_idx = (i, row_idx)
        break

def get_new_pos(pos, to_dir):
    if to_dir == 0:
        return (pos[0] - 1, pos[1]), [(pos[0], pos[1] - 1), (pos[0] + 1, pos[1] - 1)], [(pos[0], pos[1] + 1), (pos[0] + 1, pos[1] + 1)], 2
    elif to_dir == 1:
        return (pos[0], pos[1] + 1), [(pos[0] - 1, pos[1]), (pos[0] - 1, pos[1] - 1)], [(pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] - 1)], 3
    elif to_dir == 2:
        return (pos[0] + 1, pos[1]), [(pos[0], pos[1] + 1), (pos[0] - 1, pos[1] + 1)], [(pos[0], pos[1] - 1), (pos[0] - 1, pos[1] - 1)], 0
    elif to_dir == 3:
        return (pos[0], pos[1] - 1), [(pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] + 1)], [(pos[0] - 1, pos[1]), (pos[0] - 1, pos[1] + 1)], 1
    else:
        raise ValueError("Position value out of range")


def get_dir_options(pos: tuple[int, int]):
    possible_options = []
    
    for i in range(4):
        new_pos, _, _, from_dir = get_new_pos(pos, i)
        if new_pos[0] < 0 or new_pos[1] < 0:
            continue
        new_char = lines[new_pos[0]][new_pos[1]]
        char_dirs = dir_map[new_char].copy()
        if char_dirs and from_dir in char_dirs:
            possible_options.append((new_pos, new_char, from_dir))
    return possible_options

if not s_idx:
    exit()

possible_options = get_dir_options(s_idx)

paths = {i: [] for i in range(len(lines))}
paths[s_idx[0]].append(s_idx[1])
# left_idx, right_idx = [], []

steps = 1
position, char, from_direction = possible_options[0]
while char != "S":
    char_directions = dir_map[char].copy()
    char_directions.remove(from_direction)
    to_direction = char_directions[0]
    paths[position[0]].append(position[1])
    position, left, right, from_direction = get_new_pos(position, to_direction)
    char = lines[position[0]][position[1]]
    steps += 1

def transform(char):
    if char == "|":
        return "║"
    elif char == "-":
        return "═"
    elif char == "L":
        return "╚"
    elif char == "J":
        return "╝"
    elif char == "7":
        return "╗"
    elif char == "F":
        return "╔"
    elif char == ".":
        return "●"
    else:
        return char

inside_tiles = 0

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if j in paths[i]:
            print(transform(lines[i][j]), end="")
        else:
            traces = 0
            n = j - 1
            while n >= 0:
                if n in paths[i] and lines[i][n] in ["|", "F", "7", "S"]:
                    traces += 1
                n -= 1
            if traces % 2 == 0:
                print('\033[92m' + transform(lines[i][j]) + '\033[0m', end="")
            else:
                print('\033[94m' + transform(lines[i][j]) + '\033[0m', end="")
                inside_tiles += 1
    print("")

print(inside_tiles)
