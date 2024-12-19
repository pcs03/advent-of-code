from functools import cache

with open("./data/test19.txt") as file:
    patterns, designs = file.read().split("\n\n")
    patterns = set([string.strip() for string in patterns.split(",")])
    designs = designs.splitlines()

max_length = max(len(string) for string in patterns)

@cache
def lookup(design: str) -> bool:
    if len(design) == 0:
        print("Match")
        return True

    items: list[int] = []
    for i in range(1, max_length + 1):
        substring = design[:i]
        if substring in patterns:
            items.append(i)

    return any(lookup(design[item:]) for item in items)


sum = 0
for design in designs:
    print(design)
    match = lookup(design)
    if match:
        sum += 1
    print(match)
    print()

print(sum)
print(len(designs))
