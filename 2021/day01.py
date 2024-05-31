with open ("./data/day01.txt", "r") as file:
    lines = list(map(int, file.read().splitlines()))

increment_counter = 0

for i in range(3, len(lines)):
    prev = sum(lines[i - 3:i])
    curr = sum(lines[i - 2:i + 1])

    if curr > prev:
        increment_counter += 1

print(increment_counter)
