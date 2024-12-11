from functools import cache

with open("./data/day11.txt") as file:
    rocks = list(map(int, file.read().strip().split()))

print(rocks)

@cache
def apply_rule(rock: int) -> list[int]:
    rock_string = str(rock)
    rock_length = len(rock_string)

    if rock == 0:
        return [1]
    elif rock_length % 2 == 0:
        return [
            int(rock_string[0 : int(rock_length / 2)]),
            int(rock_string[int(rock_length / 2) : rock_length + 1]),
        ]
    else:
        return [rock * 2024]


def blink(rocks: list[int]) -> list[int]:
    new_rocks = []

    for rock in rocks:
        new_rocks.extend(apply_rule(rock))

    return new_rocks


for i in range(25):
    print(i)
    rocks = blink(rocks)

print(len(rocks))
