map = []
with open("input.txt") as f:
    for line in f:
        row = (list(line.strip()))
        map.append(row)

boolmap = [[True for i in range(len(map[0]))] for j in range(len(map))]
print(len(boolmap[0]), len(boolmap))
print(len(map[0]), len(map))

#LEFT
for i in range(len(boolmap)):
    max_col = 0
    for j in range(len(boolmap[0])):
        if int(map[i][j])>max_col  or j==0 or j==(len(boolmap[0])-1):
            boolmap[i][j] = False
            max_col=int(map[i][j])

#RIGHT
for i in range(len(boolmap)):
    max_col = 0
    for j in range(len(boolmap[0])-1, -1, -1):
        if int(map[i][j])>max_col or j==0 or j==(len(boolmap[0])-1):
            boolmap[i][j] = False
            max_col = int(map[i][j])

#DOWN
for i in range(len(boolmap[0])):
    max_col = 0
    for j in range(len(boolmap)):
        if int(map[j][i])>max_col or j==0 or j==(len(boolmap[0])-1):
            boolmap[j][i] = False
            max_col=int(map[j][i])

#UP
for i in range(len(boolmap)):
    max_col = 0
    for j in range(len(boolmap[0]) - 1, -1, -1):
        print(j, map[j][i], max_col)
        if int(map[j][i])>max_col or j==0 or j==(len(boolmap[0])-1):
            print("here")
            boolmap[j][i] = False
            max_col=int(map[j][i])

ctr=0
for i in boolmap:
    for j in i:
        if not j:
            ctr+=1

for i in range(99):
    print(boolmap[i])
    print(map[i])
print(boolmap)
print(ctr)