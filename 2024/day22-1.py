from functools import cache

with open("./data/day22.txt") as file:
    lines = list(map(int, file.read().splitlines()))


@cache
def mix(secret: int, value: int) -> int:
    return value ^ secret


@cache
def prune(secret: int) -> int:
    return secret % 16777216


@cache
def process_number(secret: int) -> int:
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))

    return secret


sum = 0
for number in lines:
    for i in range(10):
        number = process_number(number)
        print(number % 10)
    sum += number

print(sum)
