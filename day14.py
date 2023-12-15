from functools import cache

@cache
def roll_rocks(grid, north = True):
    rolled = []
    for line in grid:
        groups = line.split("#")
        groups = ["".join(sorted(list(group), reverse=north)) for group in groups]
        line = "#".join(groups)
        rolled.append(line)

    return tuple(rolled)

@cache
def get_weight(grid):
    weight = 0
    for line in grid:
        line_weight = 0
        for i, char in enumerate(line):
            if char == "O":
                line_weight += len(line) - i
        weight += line_weight
    return weight

@cache
def cycle(grid):
    rolled_north = roll_rocks(tuple(map("".join, zip(*grid))))
    rolled_west = roll_rocks(tuple(map("".join, zip(*rolled_north))))
    rolled_south = roll_rocks(tuple(map("".join, zip(*rolled_west))), north=False)
    rolled_east = roll_rocks(tuple(map("".join, zip(*rolled_south))), north=False)

    return tuple(map("".join, zip(*rolled_east)))

if __name__ == "__main__":
    with open("./data/day14.txt", 'r') as file:
        lines = tuple(file.read().splitlines())

    grid = tuple(map("".join, zip(*lines)))

    rolled = roll_rocks(grid)
    weight = get_weight(rolled)
    
    cycled = cycle(lines)
    
    grids = {}
    for i in range(10000):
        cycled = cycle(lines)
        weight = get_weight(cycled)
        lines = tuple(map("".join, zip(*cycled)))

        if cycled in grids:
            print(f"Cycle starts at index: {grids[cycled]}, with weight being: {weight}, length: {i - grids[cycled]}")

            remainder = (1000000000 - i - 1) % (i - grids[cycled])
            
            for i in range(remainder):
                cycled = cycle(lines)
                weight = get_weight(cycled)
                lines = tuple(map("".join, zip(*cycled)))
            print(f"Weight at 1 billion iterations: {weight}")
            break
        grids[cycled] = i


