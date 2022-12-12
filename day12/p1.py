from copy import deepcopy

EX = "ex.txt"
IN = "input.txt"
with open(IN) as f:
    grid = f.readlines()


for i in range(len(grid)):
    if "E" in grid[i]:
        end = (i, grid[i].index("E"))
    if "S" in grid[i]:
        head = (i, grid[i].index("S"))
    grid[i] = grid[i].strip().replace("E", "z").replace("S", "a")


visited = set()
next_layer = set()
ctr = 0
current_layer = set()
current_layer.add(head)
a = len(visited)
prev_a = -1
chain={}

while prev_a != a:
    for el in current_layer:
        for (dy, dx) in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            y_, x_ = el[0] + dy, el[1] + dx
            head_el = grid[el[0]][el[1]]

            if el == end:
                print(ctr)
                break

            if len(grid[0]) > x_ >= 0 \
                    and len(grid) > y_ >= 0\
                    and ord(grid[y_][x_]) <= (ord(head_el) + 1)\
                    and ( y_, x_) not in visited:
                next_layer.add((y_, x_))
                chain[(y_, x_)]=el


    visited = visited.union(current_layer)
    current_layer = next_layer.copy()
    next_layer = set()
    prev_a, a = a, len(visited)
    ctr += 1


path = []
node = end
while node!=(head):
    node = chain[node]
    path.append(node)

print(grid)
grid2 = ["o"*len(row) for row in grid]

for i in path:
    grid2[i[0]] = grid2[i[0]][:i[1]] + "X" + grid2[i[0]][i[1]+1:]

for row in grid2:
    print(row)
# 425
# 433
