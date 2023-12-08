def map_num(source: int, range_maps: list[tuple[int, int, int]]) -> int:
    for range_map in range_maps:
        if source in range(range_map[1], range_map[1] + range_map[2]):
            mapped = range_map[0] + source - range_map[1]
            return mapped
    return source

def map_range(ranges: list[tuple[int, int]], range_maps: list[tuple[int, int, int]]) -> list[tuple[int, int]]:
    dest_ranges = []

    print(ranges, range_maps)

    for source_range in ranges:
        for range_map in range_maps:
            if source_range[1] < range_map[0] or source_range[0] >= range_map[1]:
                dest_ranges.append(source_range)
            elif source_range[0] >= range_map[0] and source_range[1] <= range_map[1]:
                dest_ranges.append((source_range[0] + range_map[2], source_range[1] + range_map[2]))
            elif source_range[0] < range_map[0] and 1:
                1
    return dest_ranges


# Range layout
# (from, to, step)

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

    seed_nums = [int(x) for x in data[0].split(":")[1].strip().split(" ")]
    seed_ranges = []
    for i, num in enumerate(seed_nums):
        if i % 2 == 0:
            seed_ranges.append((num, num + seed_nums[i + 1]))

    mappings = [section.splitlines()[1:] for section in data[1:]]
    for i, section in enumerate(mappings):
        section_mappings = []
        for mapping in section:
            nums = [int(x) for x in mapping.split()]
            from_map = nums[1]
            to_map = nums[1] + nums[2]
            step_map = nums[0] - nums[1]

            section_mappings.append((from_map, to_map, step_map))
        maps[i] = section_mappings

print(maps)
print(seed_ranges)

print(map_range(seed_ranges, maps[0]))
    
