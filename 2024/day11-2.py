from functools import cache

with open("./data/day11.txt") as file:
    rocks = list(map(int, file.read().strip().split()))


@cache
def blink(rock: int, iterations: int) -> int:
    if iterations == 0:
        return 1

    if rock == 0:
        return blink(1, iterations - 1)
    elif len(str(rock)) % 2 == 0:
        rock_string = str(rock)
        rock_length = len(str(rock))
        return blink(int(rock_string[0 : int(rock_length / 2)]), iterations - 1) + blink(
            int(rock_string[int(rock_length / 2) : rock_length + 1]), iterations - 1
        )
    else:
        return blink(rock * 2024, iterations - 1)

sum = 0
for rock in rocks:
    rock_length = blink(rock, 75)
    sum += rock_length

print(sum)
