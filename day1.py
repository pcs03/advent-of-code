calibration_sum = 0

with open("./data/day1.txt", "r") as file:
    lines = file.readlines()

words = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
}

for line in lines:
    digits = []
    buffer = []

    i = 0
    while i < len(line):
        char = line[i]
        if char.isdigit():
            digits.append(char)
            buffer.clear()
            i += 1 
            continue

        buffer.append(char)
        
        word = "".join(buffer)

        for key, value in words.items():
            if key in word:
                digits.append(value)
                buffer.clear()
                print(line, word, i)
                i -= 1
                print(i)
        i += 1
    print(line, digits)
            
    if len(digits) == 1:
        num = int(str(digits[0]) + str(digits[0]))
        calibration_sum += num
    else:
        num = int(digits[0] + digits[-1])
        calibration_sum += num



print(calibration_sum)


