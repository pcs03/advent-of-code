with open("./data/day9.txt", "r") as file:
    lines = file.read().splitlines()
    inputs = []
    for i, line in enumerate(lines):
        numbers = line.split()
        inputs.append([int(num) for num in numbers])


def get_extr_value(inputs: list[int]) -> int:
    all_zero = all(num == 0 for num in inputs)

    if all_zero:
        return 0

    diff = []
    for i in range(len(inputs) - 1):
        change = inputs[i + 1] - inputs[i]
        diff.append(change)

    return inputs[0] - get_extr_value(diff)


extr_sum = 0

for line in inputs:
    extr_value = get_extr_value(line)
    extr_sum += extr_value

print(extr_sum)
