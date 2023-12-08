def map_num(source: int, range_maps: list[tuple[int, int, int]]) -> int:
    for range_map in range_maps:
        if source in range(range_map[1], range_map[1] + range_map[2]):
            mapped = range_map[0] + source - range_map[1]
            return mapped
    return source


# Map nums
# seed-soil: 0
# soil-fertilizer: 1
# fertilizer-water: 2
# water-light: 3
# light-temperature: 4
# temperature-humidity: 5
# humidity-location: 6

maps = {}
locations = []
seeds = []
seed_ranges = []
seed_location_matches = []

min_seed = 1000000000000000000

with open("./data/test.txt", "r") as file:
    data = file.read().strip().split("\n\n")

    seed_ranges_str = data[0].split(":")[1].strip().split(" ")
    print(seed_ranges_str)

    i = 0
    while i < len(seed_ranges_str):
        map_source = int(seed_ranges_str[i])
        map_range = int(seed_ranges_str[i + 1])
        
        seed_ranges.append(range(map_source, map_source + map_range))

        i += 2
    print(seed_ranges)

    range_maps = data[1:]

    for i in range(len(range_maps)):
        range_map = range_maps[i].split(":")[1].strip().splitlines()

        map_parsed = []

        for line in range_map:
            map_range = tuple(map(lambda x: int(x), line.split(" ")))
            map_parsed.append(map_range)
        maps[i] = map_parsed

def has_seed(num):
    for seed_range in seed_ranges:
        if num in seed_range:
            return True
    return False

for seed_range in seed_ranges:
    for seed in seed_range:
        source = int(seed)
        for i in range(len(maps)):
            source = map_num(source, maps[i])
        if has_seed(source) and source < min_seed:
            min_seed = source

print("min: ", min_seed)

