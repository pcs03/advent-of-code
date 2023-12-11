with open("./data/day3.txt", "r") as file:
    lines = file.read().splitlines()

number_table = {}

def is_symbol(char: str):
    if char == "." or char.isdigit():
        return False
    return True

for i, line in enumerate(lines):
    print(line)
    number_table[i] = []
    j = 0
    buffer = []
    idx = []

    while j < len(line):
        if line[j].isdigit():
            if len(buffer) == 0:
                idx.append(j)
            buffer.append(line[j])
        else:
            if len(buffer) > 0:
                idx.append(j)
                number_table[i].append((int("".join(buffer)), idx))
                buffer = []
                idx = []
        j += 1
    if len(buffer) > 0:
        idx.append(j)
        number_table[i].append((int("".join(buffer)), idx))

for k,v in number_table.items():
    print(v)
print("=" * 80)

def get_adj_values(i, j):
    from_j = j - 1 if j > 0 else 0
    to_j = j + 2 if j + 1 < len(lines[i]) else j + 1
    from_i = i - 1 if i > 0 else 0
    to_i = i + 2 if i + 1 < len(lines) else i + 1

    numbers = []

    for i in range(from_i, to_i):
        for j in range(from_j, to_j):
            for number, idx in number_table[i]:
                if j in range(idx[0], idx[1]):
                    if (number, idx) not in numbers:
                        numbers.append((number, idx))
    return [number for number, _ in numbers]

gear_ratios = 0

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "*":
            numbers = get_adj_values(i, j)
            if len(numbers) == 2:
                gear_ratios += numbers[0] * numbers[1]
print(gear_ratios)
