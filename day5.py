# Part 2 of this problem fried my brain, so I gave up.
# Logic is credited to: https://www.youtube.com/watch?v=NmxHw_bHhGM

inputs, *blocks = open("./data/day5.txt").read().split("\n\n")
inputs = list(map(int, inputs.split(":")[1].split()))

seeds = []
for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))

    new = []
    while len(seeds) > 0:
        source_start, source_end = seeds.pop()
        for a, b, c in ranges:
            dest_start = b
            dest_end = b + c
            step = a - b

            overlap_start = max(source_start, dest_start)
            overlap_end = min(source_end, dest_end)

            if overlap_start < overlap_end:
                new.append((overlap_start + step, overlap_end + step))
                if overlap_start > source_start:
                    seeds.append((source_start, overlap_start))
                if source_end > overlap_end:
                    seeds.append((overlap_end, source_end))
                break
        else:
            new.append((source_start, source_end))
    seeds = new
print(seeds)
print("minimum: ", min(seeds)[0])
