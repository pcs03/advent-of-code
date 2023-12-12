# Just like day 5, the solution to show problem was beyond my knowledge.
# Solution is courtesy of https://www.youtube.com/watch?v=g3Ms5e7Jdqo

from functools import cache

@cache
def count(springs, numbers) -> int:
    if springs == "":
        return 1 if numbers == () else 0

    if numbers == ():
        return 0 if "#" in springs else 1

    result = 0

    if springs[0] in ".?":
        result += count(springs[1:], numbers)

    if springs[0] in "#?":
        if (
            numbers[0] <= len(springs)
            and "." not in springs[: numbers[0]]
            and (numbers[0] == len(springs) or springs[numbers[0]] != "#")
        ):
            result += count(springs[numbers[0] + 1 :], numbers[1:])
    return result


with open("./data/test12.txt", "r") as file:
    lines = file.read().splitlines()

total = 0

part = 2

for line in lines:
    springs, numbers = line.split()
    numbers = tuple(map(int, numbers.split(",")))

    if part == 2:
        springs = "?".join([springs] * 5)
        numbers *= 5
    total += count(springs, numbers)
print(total)
