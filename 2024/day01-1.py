with open("./data/day01.txt") as file:
    lines = file.read().splitlines()

lists = [x.strip().split() for x in lines]

list1, list2 = zip(*lists)

list1 = sorted(list(map(int, list1)))
list2 = sorted(list(map(int, list2)))

distance_sum = 0

for i in range(len(list1)):
    distance = abs(list1[i] - list2[i])

    distance_sum += distance

print(distance_sum)
