import math

with open("./data/day14.txt") as file:
    lines = file.read().splitlines()

# Test
# grid_rows = 7
# grid_cols = 11

# Actual input
grid_rows = 103
grid_cols = 101


def get_future_position(row: int, col: int, d_row: int, d_col: int, seconds: int) -> tuple[int, int]:
    future_col = (col + seconds * d_col) % grid_cols
    future_row = (row + seconds * d_row) % grid_rows

    return future_col, future_row

future_positions: list[tuple[int, int]] = []

for line in lines:
    pos_string, vel_string = line.split(" ")
    col, row = map(int, pos_string[2:].split(","))
    d_col, d_row = map(int, vel_string[2:].split(","))

    future_position = get_future_position(row, col, d_row, d_col, 100)
    future_positions.append(future_position)

quadrants = [0, 0, 0, 0]

horizontal_border = grid_cols // 2
vertical_border =  grid_rows // 2

print(future_positions)

for pos in future_positions:
    if pos[0] < horizontal_border and pos[1] < vertical_border:
        quadrants[0] += 1
    if pos[0] < horizontal_border and pos[1] > vertical_border:
        quadrants[1] += 1
    if pos[0] > horizontal_border and pos[1] < vertical_border:
        quadrants[2] += 1
    if pos[0] > horizontal_border and pos[1] > vertical_border:
        quadrants[3] += 1

print(quadrants)
print("Product: ", math.prod(quadrants))
