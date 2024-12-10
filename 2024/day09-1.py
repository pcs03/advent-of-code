with open("./data/day09.txt") as file:
    line: list[int] = [int(num) for num in file.read().strip()]

blocks: list[int | None] = []
numbers_count = 0

for i, number in enumerate(line):
    for n in range(number):
        if i % 2 == 0:
            blocks.append(int(i / 2))
            numbers_count += 1
        else:
            blocks.append(None)


reversed_blocks = list(reversed(blocks))
reversed_blocks_counter = 0
reversed_number: int | None = reversed_blocks[reversed_blocks_counter]

compressed: list[int] = []

for i in range(numbers_count):
    block_number = blocks[i]
    if block_number is not None:
        compressed.append(block_number)
    else:
        while reversed_number is None:
            reversed_blocks_counter += 1
            reversed_number = reversed_blocks[reversed_blocks_counter]
        compressed.append(reversed_number)
        reversed_blocks_counter += 1
        reversed_number = reversed_blocks[reversed_blocks_counter]


checksum = 0

for i, number in enumerate(compressed):
    checksum += i * number

print(checksum)
