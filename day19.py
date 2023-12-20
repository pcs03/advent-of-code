with open("./data/day19.txt", "r") as file:
    workflows, parts = file.read().split("\n\n")
    workflows = workflows.splitlines()
    parts = parts.splitlines()

wfs = {}

# Tuple for storing a workflow:
# (category, condition, result)

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

def flow_range(ranges, workflow_name):
    res = ""
    for step in wfs[workflow_name]:
        if not step[0]:
            res = step[1]
            break

        if "<" in step[0]:
            cat, value = step[0].split("<")



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

ranges = {
    "x": [(1, 4001)],
    "m": [(1, 4001)],
    "a": [(1, 4001)],
    "s": [(1, 4001)],
}

for k, v in wfs.items():
    print(k, v)

print(wfs["in"])
print(wfs["zs"])
print(wfs["kp"])
print(wfs["dkr"])
