from functools import cache

with open("./data/day19.txt") as file:
    patterns, designs = file.read().split("\n\n")
    patterns = set([string.strip() for string in patterns.split(",")])
    designs = designs.splitlines()

max_length = max(len(string) for string in patterns)

@cache
def lookup(design: str, pattern: tuple[str, ...]) -> set[tuple[str, ...]]:
    if len(design) == 0:
        return {pattern}

    results = set()
    for i in range(1, max_length + 1):
        substring = design[:i]
        if substring in patterns:
            results.update(lookup(design[i:], tuple([*pattern, substring])))

    return results


sum = 0
for design in designs:
    print(design)
    match = lookup(design, ())
    if match:
        sum += len(match)
    print(match)
    print()

print(sum)
print(len(designs))
