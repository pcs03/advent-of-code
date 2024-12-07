with open("./data/day07.txt") as file:
    lines = file.read().splitlines()

values: list[tuple[int, list[int]]] = []

for line in lines:
    testvalue, numbers = line.split(":")
    values.append((int(testvalue), list(map(int, numbers.strip().split()))))

def evaluate(value: int, input: list[int], expected: int) -> bool:
    if value > expected:
        return False

    if len(input) == 1:
        return value * input[0] == expected or value + input[0] == expected

    return evaluate(value * input[0], input[1:], expected) or evaluate(
        value + input[0], input[1:], expected
    )

sum = 0
for testvalue, numbers in values:
    possible = evaluate(numbers[0], numbers[1:], testvalue)

    if possible:
        sum += testvalue

print(sum)
