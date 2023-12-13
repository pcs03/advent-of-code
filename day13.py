# "Dear Coding Deities, I come before you with a humble plea for pardon,
#  as my code resembles a labyrinth constructed by a sleep-deprived squirrel with a penchant for chaos.
#  In my misguided endeavors, 
#  I have unintentionally transformed simplicity into an enigma that even the bravest debugger dare not venture into.
#  My sincerest apologies for this coding calamity, and may the next day of the advent find favor in your divine eyes."

#  Amen.

# it did get the correct answer though, so amen to that too.

from collections import Counter

with open("./data/day13.txt", "r") as file:
    blocks = []
    for block in file.read().split("\n\n"):
        lines = block.splitlines()
        blocks.append(lines)

def walk(block, around, table) -> bool:
    up = around[0] >= len(block) - around[1] - 1

    if up:
        for i in range(around[1] + 1, len(block)):
            line = block[i]
            opposite_idx = i - (i - around[1] + 1) * 2 + 1
            if opposite_idx not in table[line]:
                return False
    else:
        for i in range(around[0] - 1, -1, -1):
            line = block[i]
            opposite_idx = i + (around[0] - i) * 2 + 1
            if opposite_idx not in table[line]:
                return False

    return True

def get_mirror(block, mutate: tuple[int, int] = (None, None), char: str = None):
    if mutate and char:
        block = block.copy()
        i, j = mutate
        block[i] = block[i][:j] + char + block[i][j + 1:]

    vertical = {
    }

    around = []

    for i, line in enumerate(block):
        try:
            vertical[line].append(i)

            for num in vertical[line]:
                if abs(i - num) == 1:
                    around.append(line)

        except KeyError:
            vertical[line] = [i]
    valid_idxs = []
    for pair in around:
        indices = vertical[pair].copy()
        pairs = []
        for idx in indices:
            for idx2 in indices:
                if abs(idx2 - idx) == 1:
                    pairs.append((min(idx, idx2), max(idx, idx2)))
                    indices.remove(idx)
                    indices.remove(idx2)
        
        for idxs in pairs:
            valid = walk(block, (idxs[0], idxs[1]), vertical)

            if valid:
                valid_idxs.append(idxs)
    return valid_idxs

out = []
tr = []
tr2 = []
line_sum = 0
for block in blocks:
    mirror = get_mirror(block)

    if not mirror:
        tr.append(1)
        transposed = []
        for i in range(len(block[0])):
            r = ""
            for j in range(len(block)):
                r += block[j][i]
            transposed.append(r)

        mirror = get_mirror(transposed)
        if not mirror:
            raise ValueError()
        else:
            out.extend([(item, 1) for item in mirror])
    else:
        out.extend([(item, 0) for item in mirror])


line_sum = 0
for n, block in enumerate(blocks):
    solutions = []
    for i in range(len(block)):
        for j in range(len(block[0])):
            char = "#" if block[i][j] == "." else "."
            mirror = get_mirror(block, (i, j), char)
            if mirror:
                solutions.extend([(item, 0) for item in mirror])
                tr2.append(0)

    transposed = []
    for i in range(len(block[0])):
        r = ""
        for j in range(len(block)):
            r += block[j][i]
        transposed.append(r)

    for i in range(len(transposed)):
        for j in range(len(transposed[0])):
            char = "#" if transposed[i][j] == "." else "."
            mirror = get_mirror(transposed, (i, j), char)
            if mirror:
                solutions.extend([(item, 1) for item in mirror])
                tr2.append(1)
        
    if not solutions:
        raise ValueError("No solutions")

    for idx, count in Counter(solutions).items():
        print()
        if idx != out[n]:
            if idx[1] == 0:
                line_sum += idx[0][1] * 100
            elif idx[1] == 1:
                line_sum += idx[0][1]

print(line_sum)


