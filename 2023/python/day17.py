from heapq import heappop, heappush

with open("./data/day17.txt", "r") as file:
    lines = file.read().splitlines()

# 2D list of heat loss numbers
grid = [list(map(int, line.strip())) for line in lines]

# Visited nodes
seen = set()

# Priority Queue. (cost, row, col, d-row, d-col, number of straight)
pq = [(0, 0, 0, 0, 0, 0)]

while pq:
    # Take the position with lowest cost from the queue
    hl, r, c, dr, dc, n = heappop(pq)

    # If goal is reached, return the cost of that goal
    if r == len(grid) - 1 and c == len(grid[0]) - 1 and n >= 4:
        print(hl)
        break

    # If out of grid bounds, skip
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        continue

    # If in seen, skip
    if (r, c, dr, dc, n) in seen:
        continue

    # Add node to seen, as i will we explored below
    seen.add((r, c, dr, dc, n))

    # Explore the possibility of travelling in a straight line from prev dir
    if n < 10 and (dr, dc) != (0, 0):
        # New position is old pos + delta pos (direction)
        nr = r + dr
        nc = c + dc
        # If new pos not out of bounds, add to the heap queue
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n + 1))

    if n >= 4 or (dr, dc) == (0, 0):
        # Explore the other possibilities
        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            # If the direction is not in a straight line of back
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr
                nc = c + ndc
                # If the new position is not out of bounds, add to the heap que
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))
