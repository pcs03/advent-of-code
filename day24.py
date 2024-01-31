from typing import Union


with open("./data/day24.txt", "r") as file:
    lines = file.read().splitlines()

    input = []
    for line in lines:
        pos, delta = line.split(" @ ")
        input.append((*list(map(float, pos.split(", "))), *list(map(float, delta.split(", ")))))

with open("./data/day24.txt", "r") as file:
    lines = file.read().splitlines()

    input = []
    for line in lines:
        pos, delta = line.split(" @ ")
        input.append((*list(map(float, pos.split(", "))), *list(map(float, delta.split(",  ")))))

space = (200000000000000, 400000000000000)

def get_intersection(x1, y1, z1, dx1, dy1, dz1, x2, y2, z2, dx2, dy2, dz2) -> Union[None, tuple[int, int]]:
    print(x1, y1, x2, y2)
    slope1 = dy1 / dx1
    yint1 = y1 - slope1 * x1

    slope2 = dy2 / dx2
    yint2 = y2 - slope2 * x2

    print(f"{slope1}x + {yint1}, {slope2}x + {yint2}")

    try:
        x_intercept = (yint2 - yint1) / (slope1 - slope2)
        y_intercept = slope1 * x_intercept + yint1
    except ZeroDivisionError:
        return None

    if x_intercept > x1 and dx1 < 0:
        return None
    if x_intercept < x1 and dx1 > 0:
        return None
    if x_intercept > x2 and dx2 < 0:
        return None
    if x_intercept < x2 and dx2 > 0:
        return None

    if y_intercept > y1 and dy1 < 0:
        return None
    if y_intercept < y1 and dy1 > 0:
        return None
    if y_intercept > y2 and dy2 < 0:
        return None
    if y_intercept < y2 and dy2 > 0:
        return None

    return (x_intercept, y_intercept)

counts = 0
for i, pos1 in enumerate(input):
    x1, y1, *_ = pos1
    for j, pos2 in enumerate(input):
        x2, y2, *_ = pos2
        if j > i:
            intersect = get_intersection(*pos1, *pos2)
            if not intersect:
                continue
            if space[0] <= intersect[0] <= space[1] and space[0] <= intersect[1] <= space[1]:
                time1 = intersect[0]
                print("pass")
                counts += 1

            else:
                print("No")
            print()
print(counts)
