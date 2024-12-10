with open("./data/day09.txt") as file:
    line: list[int] = [int(num) for num in file.read().strip()]

blocks: list[tuple[int | None, int]] = []

for i, number in enumerate(line):
    if i % 2 == 0:
        blocks.append((int(i / 2), number))
    else:
        blocks.append((None, number))

def find_id_idx(id: int) -> int:
    for i in range(len(blocks) - 1, -1, -1):
        block = blocks[i]
        if block[0] == id:
            return i

    raise RuntimeError(f"id {id} not found")


for id in range(int(len(blocks) / 2), -1, -1):
    id_idx = find_id_idx(id)
    print(id_idx)
    id_block = blocks[id_idx]
    space = id_block[1]

    for idx, block in enumerate(blocks):
        if idx >= id_idx:
            break
        if block[0] is not None:
            continue

        if block[1] >= space:
            remaining_space = block[1] - space

            blocks[id_idx] = (None, space)
            blocks.pop(idx)

            blocks.insert(idx, (None, remaining_space))
            blocks.insert(idx, (id, space))
            break

sum = 0
idx = 0
for block in blocks:
    if block[0] is None:
        idx += block[1]
        continue

    for i in range(block[1]):
        sum += idx * block[0]
        idx += 1

print(sum)





