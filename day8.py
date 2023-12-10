import math

with open("./data/day8.txt", "r") as file:
    instructions, nodes = file.read().split("\n\n")

node_table = {}
a_nodes = []

instructions = instructions.replace("R", "1").replace("L", "0")
for node in nodes.splitlines():
    from_node, to_nodes = node.split(" = (")
    to_nodes = to_nodes.replace(")", "").strip().split(", ")
    node_table[from_node] = to_nodes
    if from_node[2] == "A":
        a_nodes.append(from_node)

def while_condition(nodes):
    for node in nodes:
        if node[2] != "Z":
            return True
    return False


multiples = []

for node in a_nodes:
    steps = 0

    while node[2] != "Z":
        instruction = instructions[steps % len(instructions)]
        node = node_table[node][int(instruction)]
        steps += 1
    multiples.append(steps)

print(math.lcm(*multiples))
