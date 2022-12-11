import copy
FILE = "input.txt"
SIZE = 1200
with open(FILE) as f:
    data = [row.strip() for row in f]

grid = [["."] * SIZE for i in range(SIZE)]

rope = [[SIZE//2,SIZE//2] for i in range(10)]
# H = [4, 4]

def print_rope():
    grid2= copy.deepcopy(grid)
    for i in range(len(rope)-1, -1, -1):
        grid2[rope[i][0]][rope[i][1]] = str(i)
    for row in grid2:
        print(row)
    print()


def move_rope(i):

    if (rope[i][0] - rope[i+1][0]) > 1 and (rope[i][1] - rope[i+1][1]) > 1:
        rope[i + 1][0] = rope[i][0] - 1
        rope[i + 1][1] = rope[i][1] - 1
    elif (rope[i][0] - rope[i+1][0]) > 1 and (rope[i][1] - rope[i+1][1]) < -1:
        rope[i + 1][0] = rope[i][0] - 1
        rope[i + 1][1] = rope[i][1] + 1

    elif (rope[i][0] - rope[i+1][0]) < -1 and (rope[i][1] - rope[i+1][1]) > 1:
        rope[i + 1][0] = rope[i][0] + 1
        rope[i + 1][1] = rope[i][1] - 1

    elif (rope[i][0] - rope[i+1][0]) < -1 and (rope[i][1] - rope[i+1][1])< -1:
        rope[i + 1][0] = rope[i][0] + 1
        rope[i + 1][1] = rope[i][1] + 1

    elif (rope[i][0] - rope[i+1][0]) > 1:
        rope[i + 1][0] = rope[i][0] - 1
        rope[i + 1][1] = rope[i][1]

    elif (rope[i][0] - rope[i+1][0]) < -1:
        rope[i + 1][0] = rope[i][0] + 1
        rope[i + 1][1] = rope[i][1]

    elif (rope[i][1] - rope[i+1][1]) > 1:
        rope[i + 1][0] = rope[i][0]
        rope[i + 1][1] = rope[i][1] - 1

    elif (rope[i][1] - rope[i+1][1]) < -1:
        rope[i + 1][0] = rope[i][0]
        rope[i + 1][1] = rope[i][1] + 1


for el in data:
    parts = el.split()
    for i in range(int(parts[1])):
        if (parts[0]) == "R":
            rope[0][1] += 1
        if (parts[0]) == "L":
            rope[0][1] -= 1

        if (parts[0]) == "U":
            rope[0][0] -= 1
        if (parts[0]) == "D":
            rope[0][0] += 1

        for i in range(9):
            dist = (rope[i][0] - rope[i + 1][0]) ** 2 + (rope[i][1] - rope[i + 1][1]) ** 2
            if dist > 2:
                move_rope(i)
        grid[rope[9][0]][rope[9][1]] = "#"
ctr = 0

for row in grid:
    for el in row:
        if el == "#":
            ctr += 1

print(ctr)
