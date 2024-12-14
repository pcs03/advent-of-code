import math
from collections import Counter

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

def calculate_local_entropy(char_list: list[str], window_size=3):
    if window_size > len(char_list):
        raise ValueError("Window size must be less than or equal to the length of the input list.")
    
    total_entropy = 0
    num_windows = 0

    # Slide over the list with the given window size
    for i in range(len(char_list) - window_size + 1):
        window = char_list[i:i + window_size]
        # Calculate Shannon entropy for the current window
        char_count = Counter(window)
        total_chars = len(window)
        entropy = -sum((count / total_chars) * math.log2(count / total_chars) for count in char_count.values())
        total_entropy += entropy
        num_windows += 1

    # Average entropy over all windows
    return total_entropy / num_windows if num_windows > 0 else 0

entropy_list: list[float] = []

for i in range(10000):
    future_positions: set[tuple[int, int]] = set()
    print("Seconds: ", i)
    for line in lines:
        pos_string, vel_string = line.split(" ")
        col, row = map(int, pos_string[2:].split(","))
        d_col, d_row = map(int, vel_string[2:].split(","))

        future_position = get_future_position(row, col, d_row, d_col, i)
        future_positions.add(future_position)

    grid: list[str] = []

    for row in range(grid_rows):
        for col in range(grid_cols):
            if (col, row) in future_positions:
                grid.append("#")
            else:
                grid.append(" ")

    entropy = calculate_local_entropy(grid)
    entropy_list.append(entropy)

    print(i, entropy)

lowest_entropy = min(entropy_list)
seconds = entropy_list.index(lowest_entropy)
print(seconds)



