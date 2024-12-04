with open("./data/day04.txt") as file:
    lines = list(map(list, file.read().splitlines()))

directions = {
    "f": ["MASMAS", "MASSAM"],
    "b": ["SAMSAM", "SAMMAS"]
}

pattern = [(1, 1), (1, 1), (0, -2), (-1, 1), (-1, 1)]

def trace_word(i, j, letter_number, word):
    di, dj = pattern[letter_number - 1]
    new_i = i + di
    new_j = j + dj

    if new_i < 0 or new_i >= len(lines) or new_j < 0 or new_j >= len(lines[0]):
        return 0

    expected_letter = word[letter_number]

    if lines[new_i][new_j] == expected_letter:
        if letter_number == 5:
            return 1
        return trace_word(new_i, new_j, letter_number + 1, word)
    else:
        return 0

sum = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        letter = lines[i][j]
        if letter == "M":
            sum += trace_word(i, j, 1, "MASMAS")
            sum += trace_word(i, j, 1, "MASSAM")
        elif letter == "S":
            sum += trace_word(i, j, 1, "SAMSAM")
            sum += trace_word(i, j, 1, "SAMMAS")

print(sum)




