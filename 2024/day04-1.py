with open("./data/day04.txt") as file:
    lines = list(map(list, file.read().splitlines()))

print(lines)

word = "XMAS"

directions = {
    "n": (-1, 0),
    "ne": (-1, 1),
    "e": (0, 1),
    "se": (1, 1),
    "s": (1, 0),
    "sw": (1, -1),
    "w": (0, -1),
    "nw": (-1, -1),
}

def trace_word(i, j, direction, letter_number):
    di, dj = directions[direction]
    new_i = i + di
    new_j = j + dj

    if new_i < 0 or new_i >= len(lines) or new_j < 0 or new_j >= len(lines[0]):
        return 0

    expected_letter = word[letter_number]

    if lines[new_i][new_j] == expected_letter:
        if expected_letter == "S":
            return 1
        return trace_word(new_i, new_j, direction, letter_number + 1)
    else:
        return 0

def trace_all_directions(i, j) -> int:
    # Trace all directions if i,j contains "X"
    if lines[i][j] != "X":
        raise RuntimeError("Expected X on position")

    sum = 0

    for direction in directions:
        is_word = trace_word(i, j, direction, 1)
        sum += is_word

        if is_word != 0:
            print(i, j, direction)

    return sum


sum = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "X":
            sum += trace_all_directions(i, j)


print(sum)



