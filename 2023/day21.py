with open("./data/test21.txt", "r") as file:
    grid = file.read().splitlines()

queue = set()

for row, line in enumerate(grid):
    col = line.find("S")
    if col != -1:
        queue.add((row, col))

steps = 0

for i in range(0, 200):
    new_queue = set()
    length = len(queue)
    while queue:
        pos = queue.pop()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dir in directions:
            new_pos = (pos[0] + dir[0], pos[1] + dir[1])
            rem_pos = (new_pos[0] % len(grid), new_pos[1] % len(grid[0]))

            char = grid[rem_pos[0]][rem_pos[1]]

            if char == "#":
                continue
            elif char == "." or char == "S":
                new_queue.add(new_pos)
            else:
                raise RuntimeError
    print(i + 1, len(new_queue) - length, len(new_queue) / length)
    queue = new_queue
