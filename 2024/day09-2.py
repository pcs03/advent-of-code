with open("./data/day09.txt") as file:
    line: list[int] = [int(num) for num in file.read().strip()]

blocks: list[tuple[int, int | None]] = []
numbers_count = 0

print(len(line))

for i, number in enumerate(line):
    if i % 2 == 0:
        blocks.append((number, int(i / 2)))
    else:
        blocks.append((number, None))

print(len(blocks))

# checksum = 0
#
# for i, number in enumerate(compressed):
#     checksum += i * number
#
# print(checksum)


