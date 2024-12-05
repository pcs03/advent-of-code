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


def fix_list_items(update: list[int]) -> tuple[bool, list[int]]:
    correct = True

    for lower, upper in ordering:
        try:
            lower_index = update.index(lower)
            upper_index = update.index(upper)
        except ValueError:
            continue

        if lower_index > upper_index:
            correct = False
            lower_number = update.pop(lower_index)
            update.insert(upper_index, lower_number)

    return correct, update

def get_middle_number(update: list[int]):
    return update[int(len(update) / 2)]
            

sum = 0
for update in updates:
    initial_correct = check_update_ordering(update)
    correct = initial_correct

    while not correct:
        correct, update = fix_list_items(update)

    if not correct:
        print("no", update)

    if not initial_correct:
        sum += get_middle_number(update)


print(sum)

