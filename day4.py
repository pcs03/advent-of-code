import re


with open("./data/day4.txt", "r") as file:
    lines = file.read().strip().splitlines()

sum = 0

map = {num: 1 for num in range(1, len(lines) + 1)}

for line in lines:
    card_num = int(re.findall(r'\d+', line.split(":")[0])[0])
    numbers = line.split(":")[1].strip()
    win_nums = numbers.split("|")[0].strip().split()
    nums = numbers.split("|")[1].strip().split()

    count = 0
    
    for num in nums:
        if num in win_nums:
            count += 1

    for i in range(map[card_num]):
        for j in range(card_num + 1, card_num + count + 1):
            try:
                map[j] += 1
            except KeyError:
                continue

print(map)
for value in map.values():
    sum += value
print(sum)
