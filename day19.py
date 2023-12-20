from math import prod

with open("./data/day19.txt", "r") as file:
    workflows, parts = file.read().split("\n\n")
    workflows = workflows.splitlines()
    parts = parts.splitlines()

wfs = {}

for workflow in workflows:
    wf_name, wf_string = workflow.split("{")
    wf_string = wf_string[:-1]
    wf_list = wf_string.split(",")
    seq = []
    for item in wf_list:
        if "<" in item or ">" in item:
            condition, result = item.split(":")
            seq.append((condition, result))
        else:
            seq.append((None, item))
    wfs[wf_name] = seq


# Beautiful recursive function for part 1
def flow(ratings, workflow_name):
    res = ""
    for step in wfs[workflow_name]:
        if not step[0]:
            res = step[1]
            break

        if "<" in step[0]:
            cat, value = step[0].split("<")
            if ratings[cat] < int(value):
                res = step[1]
                break

        if ">" in step[0]:
            cat, value = step[0].split(">")
            if ratings[cat] > int(value):
                res = step[1]
                break

    if res == "A":
        return sum(ratings.values())
    elif res == "R":
        return 0
    else:
        return flow(ratings, res)

# Less beautiful, but still functional, recursive function for part 2
# BTW, does someone has medication for off-by-one-error-induced depression? Would love to take some after writing this
def flow_range(ranges, workflow_name):
    result_sum = 0
    if workflow_name == "A":
        return prod(len(r) for r in ranges.values())
    if workflow_name == "R":
        return 0

    for step in wfs[workflow_name]:
        if not step[0]:
            result_sum += flow_range(ranges, step[1])
            continue

        if "<" in step[0]:
            cat, value = step[0].split("<")
            value = int(value)
            r = ranges[cat]

            if r[0] >= value:
                continue
            if r[-1] < value:
                return flow_range(ranges, step[1])
            elif r[0] < value and r[-1] >= value:
                lower = range(r[0], value)
                upper = range(value, r[-1] + 1)

                result_sum += flow_range({**ranges, cat: lower}, step[1])
                ranges[cat] = upper
            else:
                raise RuntimeError

        elif ">" in step[0]:
            cat, value = step[0].split(">")
            value = int(value)
            r = ranges[cat]

            if r[-1] <= value:
                continue
            if r[0] > value:
                return flow_range(ranges, step[1])
            elif r[0] <= value and r[-1] > value:
                lower = range(r[0], value + 1)
                upper = range(value + 1, r[-1] + 1)

                result_sum += flow_range({**ranges, cat: upper}, step[1])
                ranges[cat] = lower
            else:
                raise RuntimeError
        else:
            raise RuntimeError
    return result_sum


ranges = {
    "x": range(1, 4001),
    "m": range(1, 4001),
    "a": range(1, 4001),
    "s": range(1, 4001),
}

print(flow_range(ranges, "in"))
