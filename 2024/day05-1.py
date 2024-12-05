with open("./data/day05.txt") as file:
    sections = list(map(lambda x: x.split("\n"), file.read().strip().split("\n\n")))

ordering = [tuple(map(int, item.split("|"))) for item in sections[0]]
updates = [list(map(int, update.split(","))) for update in sections[1]]

def check_update_ordering(update: list[int]):
    map = {item: index for index, item in enumerate(update)} 

    for lower, upper in ordering:
        lower_index = map.get(lower, None)
        upper_index = map.get(upper, None)

        if lower_index is None or upper_index is None:
            continue

        if lower_index > upper_index:
            return False
    
    return True

def get_middle_number(update: list[int]):
    return update[int(len(update) / 2)]
            

sum = 0
for update in updates:
    correct = check_update_ordering(update)

    if correct:
        sum += get_middle_number(update)

    print(update, correct)

print(sum)

