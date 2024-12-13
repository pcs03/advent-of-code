with open("./data/day13.txt") as file:
    lines = [tuple(line.splitlines()) for line in file.read().split("\n\n")]

equations = []
for line in lines:
    a_string, b_string, res_string = line

    a = tuple(int(number[2:]) for number in a_string[10:].split(", "))
    b = tuple(int(number[2:]) for number in b_string[10:].split(", "))
    res = tuple(int(number[2:]) for number in res_string[7:].split(", "))

    equations.append([a, b, res])

sum = 0

for a, b, res in equations:
    x1, y1 = a
    x2, y2 = b
    xsum, ysum = res

    xsum += 10000000000000
    ysum += 10000000000000

    b = (x1 * ysum - y1 * xsum) / (x1 * y2 - y1 * x2)

    if not b.is_integer() or b < 0:
        continue
    
    b = int(b)

    a = (xsum - x2 * b) / x1

    if not a.is_integer() or a < 0:
        continue

    a = int(a)

    cost = a * 3 + b * 1
    sum += cost

print(sum)

