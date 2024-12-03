import re
from functools import reduce
from operator import mul as multiply

with open("./data/day03.txt") as file:
    input = file.read()

print(input)

instructions = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don\'t\(\))", input)

print(instructions)

do = True
mul_sum = 0

for item in instructions:
    if item == "do()":
        do = True
        continue
    if item == "don't()":
        do = False
        continue

    if do:
        numbers = re.findall(r'\d+', item)

        if len(numbers) != 2:
            raise ValueError("Expected 2 numbers")

        numbers = map(int, numbers)
        mul_sum += reduce(multiply, numbers)

print(mul_sum)
