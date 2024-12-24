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


banana_sums: dict[tuple[int, ...], int] = {}

total_changes: dict[tuple[int, ...], int] = {}
sum = 0
for number in lines:
    print(number)
    price = number % 10
    prev_price = price

    prices: list[int] = [number % 10]
    changes: list[int] = []

    patterns: dict[tuple[int, ...], int] = {}

    for i in range(1999):
        number = process_number(number)
        price = number % 10
        prices.append(price)
        changes.append(price - prev_price)
        prev_price = price

        if len(changes) >= 4:
            pattern = tuple(changes[i - 3: i + 1])
            if pattern not in patterns:
                patterns[pattern] = price

    for pattern, price in patterns.items():
        try:
            banana_sums[pattern] += price
        except KeyError:
            banana_sums[pattern] = price

    sum += number

best_pattern = max(banana_sums, key=banana_sums.get)
print(best_pattern, banana_sums[best_pattern])

