with open("./data/day08.txt") as file:
    grid = [list(line) for line in file.read().splitlines()]


def find_antennas(grid: list[list[str]]) -> dict[str, set[tuple[int, int]]]:
    antennas: dict[str, set[tuple[int, int]]] = {}

    for col in range(len(grid)):
        for row in range(len(grid[0])):
            char = grid[col][row]

            if char == ".":
                continue

            try:
                antennas[char].add((col, row))
            except KeyError:
                antennas[char] = set([(col, row)])

    return antennas


antennas = find_antennas(grid)

antinodes: set[tuple[int, int]] = set()

for antenna_type, positions in antennas.items():
    covered: set[tuple[int, int]] = set()
    print(antenna_type)

    for pos_a in positions:
        for pos_b in positions:
            if pos_a == pos_b or pos_b in covered:
                continue

            d_col = pos_b[0] - pos_a[0]
            d_row = pos_b[1] - pos_a[1]

            new_antinodes: list[tuple[int, int]] = []

            for i in range(100):
                new_antinodes.extend([
                    (pos_b[0] + i * d_col, pos_b[1] + i * d_row),
                    (pos_a[0] - i * d_col, pos_a[1] - i * d_row),
                ])

            for node in new_antinodes:
                if node[0] < 0 or node[0] >= len(grid) or node[1] < 0 or node[1] >= len(grid[0]):
                    continue
                antinodes.add(node)

        covered.add(pos_a)

print(len(antinodes))
