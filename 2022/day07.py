lines = iter(open("./data/test07.txt", "r"))
for line in lines:
    next(lines)
    print(line)
