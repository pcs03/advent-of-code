import re
from functools import reduce
from operator import mul as multiply

with open("./data/day03.txt") as file:
    input = file.read()

muls = re.findall(r'mul\(\d+,\d+\)', input)
mul_sum = 0

for mul in muls:
    numbers = re.findall(r'\d+', mul)

    if len(numbers) != 2:
        raise ValueError("Expected 2 numbers")

    numbers = map(int, numbers)
    mul_sum += reduce(multiply, numbers)

print(mul_sum)
