lines = iter(open("./data/test07.txt", "r"))

struc = {}
pos = []

for line in lines:
    print(line)
    if line[0] == "$":
        
        command = line[2:].split()
        print(command)

        if command[0] == "cd":
            if command[1] == "..":
                pos = pos[:-1]
            else:
                pos.append(command[1])

        if command[0] == "ls":
            if len(command) != 1:
                raise RuntimeError("ls command has more than one argument.")

            while True:
                next(lines)
                if line[0] == '$':
                    break
                output = line.split()




    print("POS", pos)
    # next(lines)
    # print(line
