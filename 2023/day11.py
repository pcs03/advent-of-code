with open("./data/day11.txt", "r") as file:
    lines = file.read().splitlines()

empty_rows = [i for i in range(len(lines)) if "#" not in lines[i]]
empty_cols = [j for j in range(len(lines[0])) if "#" not in [line[j] for line in lines]]

input = []
counter = 1
idx = {}

# Expand the universe
for i in range(len(lines)):
    line = []
    for j in range(len(lines[0])):
        if lines[i][j] == "#":
            line.append(str(counter))
            idx[counter] = (i, j)
            counter += 1
        else:
            line.append(".")

    input.append(line)

# Calculate pairs
pairs = []
for i in range(1, counter):
    for j in range(1, counter - 1):
        if i != j and j < i:
            pairs.append((i, j))

def get_distance(num1, num2):
    empty_length = 1000000

    idx1 = idx[num1]
    idx2 = idx[num2]
    range_i = (sorted([idx1[0], idx2[0]]))
    range_j = (sorted([idx1[1], idx2[1]]))

    distance = abs(range_j[1] - range_j[0]) + abs(range_i[1] - range_i[0])
    empty_dist = 0

    for row in empty_rows:
        if row in range(*range_i):
            empty_dist += 1
    for col in empty_cols:
        if col in range(*range_j):
            empty_dist += 1

    return distance + empty_dist * (empty_length - 1)

total_distance = 0
for pair in pairs:
    distance = get_distance(pair[0], pair[1])
    total_distance += distance
print(total_distance)
