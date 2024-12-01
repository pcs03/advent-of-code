with open("./data/day06.txt", "r") as file:
    line = file.read().strip()

for i in range(13, len(line)):
    chars = "".join(line[i - 13:i + 1])

    if len(chars) == len(set(chars)):
        print(i + 1)
        print(chars)
        break


