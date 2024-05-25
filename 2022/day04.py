with open("./data/day04.txt", "r") as file:
    lines = file.read().splitlines()

total = 0

for line in lines:
    sections = []
    textsections = line.split(",")
    for section in textsections:
        start, end = map(int, section.split("-"))
        sections.append((start, end))

    # if (sections[0][0] <= sections[1][0] and sections[0][1] >= sections[1][1]) or (
    #     sections[1][0] <= sections[0][0] and sections[1][1] >= sections[0][1]
    # ):
    #     print(sections)
    #     total += 1

    if not (sections[0][0] > sections[1][1] or sections[0][1] < sections[1][0]):
        print(sections)
        total += 1

print(total)
