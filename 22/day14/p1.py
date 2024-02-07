EX = "ex.txt"
IN = "input.txt"

grid = [["." for i in range(1000)] for j in range(1000)]

with open(IN) as f:
    data = [row.strip() for row in f]

lowest_wall = 0
for row in data:
    lines = row.split(" -> ")
    for i in range(1, len(lines)):
        a, b = lines[i - 1].split(","), lines[i].split(",")
        ay, ax = int(a[0]), int(a[1])
        by, bx = int(b[0]), int(b[1])
        lowest_wall = max(ax, bx, lowest_wall)
        if bx == ax:
            for j in range(min(ay, by), max(ay, by) + 1):
                grid[bx][j] = "#"
        elif ay == by:
            for j in range(min(ax, bx), max(ax, bx) + 1):
                grid[j][ay] = "#"


def drop_sand(x, y, min_floor):
    while y < min_floor:
        if grid[y+1][x] != "#" and grid[y+1][x] != "+":
            y += 1
        elif grid[y + 1][x - 1] != "#" and grid[y + 1][x - 1] != "+":
            x -= 1
            y += 1
        elif grid[y + 1][x + 1] != "#" and grid[y + 1][x + 1] != "+":
            x += 1
            y += 1
        else:
            grid[y][x] = "+"
            return True
    return False


ctr = 0
while drop_sand(500, 0, lowest_wall):
    ctr += 1
print(ctr)
