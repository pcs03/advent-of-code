import re


with open("./data/day05.txt", "r") as file:
    cratelines, moves = map(lambda section: section.splitlines(), file.read().split("\n\n"))


cratelines = cratelines[:-1]

num_stacks = int((len(cratelines[0]) + 1) / 4)
crates = [[] for _ in range(num_stacks)]

for line in cratelines:
    for i in range(0, len(line), 4):
        cratename = line[i + 1]
        crateindex = int(i / 4)

        if cratename != " ":
            crates[crateindex].insert(0, cratename)

print(crates)

for line in moves:
    print(line)
    numbers = list(map(int, re.findall(r'\d+', line)))
    num_crates = numbers[0]
    origin_stack = crates[numbers[1] - 1]
    dest_stack = crates[numbers[2] - 1]


    popped_stacks = origin_stack[-num_crates:]
    
    crates[numbers[1] - 1] = origin_stack[:-num_crates]
    dest_stack.extend(popped_stacks)
    crates[numbers[2] - 1] = dest_stack

    print(num_crates, popped_stacks)

    print(crates)

    


print(crates)

message = "".join([stack[-1] for stack in crates])
print(message)
