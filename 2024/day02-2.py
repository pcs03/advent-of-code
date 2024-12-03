with open("./data/day02.txt", "r") as file:
    lines = file.read().splitlines()

reports = [list(map(int, line.split())) for line in lines]

print(reports)

num_safe_reports = 0

def is_flipped_change_direction(change, prev_change):
    if (change >= 0 and prev_change >= 0) or (change <= 0 and prev_change <= 0):
        return False

    return True

def is_safe_report(report):
    num_flips = 0
    prev_change = 0
    safe = True

    for i in range(len(report) - 1):
        num = report[i]
        next_num = report[i + 1]
        change = num - next_num

        if abs(change) < 1 or abs(change) > 3:
            safe = False

        num_flips += is_flipped_change_direction(change, prev_change)

        prev_change = change
    

    if num_flips == 0 and safe:
        return True

    return False



for report in reports:
    if is_safe_report(report):
        num_safe_reports += 1
    else:
        for i in range(len(report)):
            new_report = report[:i] + report[i + 1:]
            if is_safe_report(new_report):
                num_safe_reports += 1
                break


print(num_safe_reports)
