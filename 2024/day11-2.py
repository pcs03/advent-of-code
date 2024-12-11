from functools import cache
import math

with open("./data/day11.txt") as file:
    rocks = list(map(int, file.read().strip().split()))


@cache
def get_rock_length(rock: int) -> int:
    return math.floor(math.log10(rock)) + 1


@cache
def split_rock(rock: int, rock_length: int) -> tuple[int, int]:
    a: int = rock // 10 ** (rock_length // 2)
    b: int = rock % 10 ** (rock_length // 2)

    return a, b


@cache
def blink(rock: int, iterations: int) -> int:
    if iterations == 0:
        return 1

    if rock == 0:
        return blink(1, iterations - 1)

    rock_length = get_rock_length(rock)

    if rock_length % 2 == 0:
        a, b = split_rock(rock, rock_length)

        return blink(a, iterations - 1) + blink(b, iterations - 1)

    return blink(rock * 2024, iterations - 1)


sum = 0
for rock in rocks:
    rock_length = blink(rock, 450)
    sum += rock_length

print(sum)
