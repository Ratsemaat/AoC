import re

EX = "ex.txt"
IN = "input.txt"

grid = [["." for i in range(1000)] for j in range(1000)]

points = set()
total = 0

with open(IN) as f:
    data = [map(int, row.strip().split(",")) for row in f]

for a, b, c in data:
    points.add((a, b, c))


def is_surrounded(point, r, visited):
    if point in visited or point in points:
        return True

    visited.add(point)
    if r == 0:
        return False

    a, b, c = point

    return is_surrounded((a + 1, b, c), r - 1, visited) and is_surrounded((a - 1, b, c), r - 1, visited) \
           and is_surrounded((a, b + 1, c), r - 1, visited) and is_surrounded((a, b - 1, c), r - 1, visited) \
           and is_surrounded((a, b, c + 1), r - 1, visited) and is_surrounded((a, b, c - 1), r - 1, visited)


outer_points = set()


for a in range(20):
    for b in range(20):
        for c in range(20):
            if is_surrounded((a, b, c), 950, set()):
                outer_points.add((a, b, c))


outer = set()
for a, b, c in outer_points:
    if (a, b, c) not in outer:
        total += 6
        for i in ((a - 1, b, c), (a + 1, b, c), (a, b - 1, c), (a, b + 1, c), (a, b, c - 1), (a, b, c + 1)):
            if i in outer:
                total -= 2
        outer.add((a, b, c))

print(total)
