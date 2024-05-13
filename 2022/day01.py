with open("./data/day01.txt", "r") as file:
    input = file.read().split("\n\n")


elves = []
for item in input:
    calories = sum(map(int, item.splitlines()))
    elves.append(calories)


elves = sorted(elves, reverse=True)
print(sum(elves[0:3]))
