import math

def get_roots(total_time, record_dist):
    dist_to_beat = record_dist + 0.00001
    charge_time_1 = (total_time - math.sqrt(total_time**2 - 4 * dist_to_beat)) / (2)
    charge_time_2 = (total_time + math.sqrt(total_time**2 - 4 * dist_to_beat)) / (2)

    return charge_time_1, charge_time_2

with open("./data/day6.txt", "r") as file:
    lines = file.read().strip().splitlines()
    times = [int(lines[0].split(":")[1].replace(" ", ""))]
    records = [int(lines[1].split(":")[1].replace(" ", ""))]
print(times, records)

num_ways_product = 1
for time, record in zip(times, records):
    roots = get_roots(time, record)
    winning_range = range(math.ceil(roots[0]), math.ceil(roots[1]))
    num_ways_product *= len(winning_range)
    print(roots, winning_range, num_ways_product)
print(num_ways_product)
