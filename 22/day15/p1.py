EX = "ex.txt"
IN = "input.txt"

grid = [["." for i in range(1000)] for j in range(1000)]

with open(IN) as f:
    data = [row.strip() for row in f]

pairs = []
for row in data:
    parts = row.split(":")
    x1, y1 = int(parts[0][12:].split(",")[0]), int(parts[0].split("=")[2])
    x2, y2 = int(parts[1][24:].split(",")[0]), int(parts[1].split("=")[2])
    pairs.append(((x1, y1), (x2, y2)))

occupied=set()


TARGET=2000000
for pair in pairs:
    dist = abs(pair[0][0]-pair[1][0]) + abs(pair[0][1]-pair[1][1])
    sx, sy = pair[0]
    if dist > abs(TARGET-sy):
        diff = dist - abs(TARGET - sy)
        for i in range(diff+1):
            occupied.add((sx + i, TARGET))
            occupied.add((sx - i, TARGET))


occupied.difference_update(set([pair[0] for pair in pairs]))
occupied.difference_update(set([pair[1] for pair in pairs]))

print(len(occupied))

