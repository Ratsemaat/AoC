FILE = "input.txt"
SIZE=1000
with open(FILE) as f:
    data = [row.strip() for row in f]

grid = [["."] * SIZE for i in range(SIZE)]

T = [4, 4]
H = [4, 4]
s = [4, 4]


def move_tail():
    if (H[0] - T[0]) > 1:
        T[0] = H[0] - 1
        T[1] = H[1]

    elif (H[0] - T[0]) < -1:
        T[0] = H[0] + 1
        T[1] = H[1]

    elif (H[1] - T[1]) > 1:
        T[0] = H[0]
        T[1] = H[1] - 1

    elif (H[1] - T[1]) < -1:
        T[0] = H[0]
        T[1] = H[1] + 1


for el in data:
    parts = el.split()
    for i in range(int(parts[1])):
        if (parts[0]) == "R":
            H[1] +=  1
        if (parts[0]) == "L":
            H[1] -= 1

        if (parts[0]) == "U":
            H[0] -= 1
        if (parts[0]) == "D":
            H[0] += 1

        dist = (H[0] - T[0]) ** 2 + (H[1] - T[1]) ** 2
        if dist > 2:
            move_tail()

        grid[T[0]][T[1]] = "#"


ctr=0

for row in grid:
    for el in row:
        if el=="#":
            ctr += 1

print(ctr)