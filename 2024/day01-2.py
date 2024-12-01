with open("./data/day01.txt") as file:
    lines = file.read().splitlines()

lists = [x.strip().split() for x in lines]
list1, list2 = zip(*lists)
list1 = map(int, list1)
list2 = map(int, list2)


number_counts_list2 = {}

for num in list2:
    try:
        number_counts_list2[num] += 1
    except KeyError:
        number_counts_list2[num] = 1

        
score_sum = 0
for num in list1:
    num_counts = number_counts_list2.get(num, 0)

    score = num_counts * num
    score_sum += score

    print(score)

print(score_sum)
