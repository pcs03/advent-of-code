with open('./data/day3.txt', "r") as file:
    lines = file.read().strip().splitlines()

sum = 0

def is_symbol(char) -> bool:
    if char == ".":
        return False
    if char.isdigit():
        return False

    return True

def is_engine(row_index, col_idx_start, col_idx_end) -> bool:
    col_idx_start = col_idx_start if col_idx_start == 0 else col_idx_start - 1
    col_idx_end = col_idx_end if col_idx_end == len(lines[row_index]) else col_idx_end + 1

    print(row_index, col_idx_start, col_idx_end)

    if is_symbol(lines[row_index][col_idx_start]) or is_symbol(lines[row_index][col_idx_end]):
        return True

    if row_index - 1 >= 0:
        for char in lines[row_index - 1][col_idx_start:col_idx_end + 1]:
            if is_symbol(char):
                return True
    
    if row_index + 1 < len(lines):
        for char in lines[row_index + 1][col_idx_start:col_idx_end + 1]:
            if is_symbol(char):
                return True

    return False    

for i, line in enumerate(lines):
    print(lines[i - 1] if i > 0 else "")
    print(line)
    print(lines[i + 1] if i + 1 <= len(lines) - 1 else "")
    
    j = 0
    while j < len(line) - 1:
        if line[j].isdigit():
            num = ""
            start_idx = j
            end_idx = None

            while line[j].isdigit():
                num += line[j]
                if j >= len(line) - 1:
                    break
                j += 1
                print("j: ", j)

            end_idx = j - 1
            print(num, end=" ")
            if is_engine(i, start_idx, end_idx):
                sum += int(num)
                print("true", sum)
            else:
                print("false")
        else:
            j += 1
        


print(sum)







