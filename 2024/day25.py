with open("./data/day25.txt") as file:
    sections = list(map(lambda section: section.splitlines(), file.read().strip().split("\n\n")))

def get_number(section: list[str]) -> tuple[int, ...]:
    section_list = [list(line) for line in section]
    t: list[list[str]] = list(zip(*section_list))

    return tuple(line.count("#") - 1 for line in t)

def test_fit(lock: tuple[int, ...], key: tuple[int, ...]) -> bool:
    length = len(lock)
    for i in range(length):
        if lock[i] + key[i] > length:
            return False

    return True

locks: set[tuple[int, ...]] = set()
keys: set[tuple[int, ...]] = set()

for section in sections:
    number = get_number(section)
    if section[0] == "#####":
        locks.add(number)
    else:
        keys.add(number)

fits = 0

for lock in list(locks):
    for key in list(keys):
        if test_fit(lock, key):
            fits += 1
print(fits)
