with open("./data/day18.txt", "r") as file:
    lines = file.read().splitlines()

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1),
}

grid_to_line = {
    "RD": (0, 1),
    "RU": (0, 0),
    "LD": (1, 1),
    "LU": (1, 0),
    "DR": (0, 1),
    "DL": (1, 1),
    "UR": (0, 0),
    "UL": (1, 0),
}


def cross(p1, p2) -> int:
    return p1[1] * p2[0] - p1[0] * p2[1]


def shoelace(points) -> int:
    sum = 0
    for i in range(0, len(points) - 1):
        sum += cross(points[i], points[i + 1])
    return (sum + cross(points[-1], points[0])) / 2


origin = (0, 0)
points = []
dir = "U"
for line in lines:
    _, _, color = line.split()
    color = color[2:-1]

    match color[-1]:
        case "0":
            new_dir = "R"
        case "1":
            new_dir = "D"
        case "2":
            new_dir = "L"
        case "3":
            new_dir = "U"
    to_line = grid_to_line[dir + new_dir]
    points.append((origin[0] + to_line[0], origin[1] + to_line[1]))

    dir = new_dir
    direction = directions[dir]
    count = int(color[:5], 16)

    position = (
        origin[0] + direction[0] * int(count),
        origin[1] + direction[1] * int(count),
    )
    origin = position

area = int(shoelace(points))
print(f"Total area: {area}")


# Flood fill algorithm for part 1, was actually quite proud of this one..
# Then they hit you with part 2, rendering using this practically impossible

# start = (1, 1)
# seen = set([start])
# queue = [start]
#
# while queue:
#     position = queue.pop(0)
#     for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#         new_position = (position[0] + dir[0], position[1] + dir[1])
#         if new_position in border:
#             continue
#
#         if new_position not in seen:
#             seen.add(new_position)
#             queue.append(new_position)


# print(f"Total: {len(border) + len(seen)}, ({len(border)} + {len(seen)}))")
