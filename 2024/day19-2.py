from functools import cache

with open("./data/day19.txt") as file:
    patterns, designs = file.read().split("\n\n")
    patterns = set([string.strip() for string in patterns.split(",")])
    designs = designs.splitlines()

max_length = max(len(string) for string in patterns)

@cache
def lookup(design: str) -> int:
    if len(design) == 0:
        raise ValueError("design cannot be empty")

    total = 0
    for length in range(1, min(max_length + 1, len(design) + 1)):
        substring = design[:length]
        rest = design[length:]

        if substring in patterns:
            if len(rest) == 0:
                total += 1
            else:
                total += lookup(rest)

    return total


sum = 0
for design in designs:
    number_matches = lookup(design)
    sum += number_matches
    
print(sum)
