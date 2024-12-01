with open("./data/day03.txt", "r") as file:
    lines = file.read().splitlines()

def get_item_value(item: str):
    if str.isupper(item):
        item = item.lower()
        value = ord(item) - 96
        return value + 26
    else:
        return ord(item) - 96

sum = 0

for i in range(0, len(lines), 3):
    sections = lines[i:i+3]
    

    compartments = [{}, {}, {}]


    for i, section in enumerate(sections):
        for item in section:
            if compartments[i].get(item):
                compartments[i][item] += 1
            else:
                compartments[i][item] = 1

    for key in compartments[0]:
        if key in compartments[1] and key in compartments[2]:

            print(key)
            print(get_item_value(key))
            sum += get_item_value(key)


print(sum)
