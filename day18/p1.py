import re

EX = "ex.txt"
IN = "input.txt"

grid = [["." for i in range(1000)] for j in range(1000)]

existing = set()
total = 0

with open(IN) as f:
    data = [map(int,row.strip().split(",")) for row in f]

for a,b,c in data:
    if (a, b, c) not in existing:
        total += 6
        for i in ((a - 1, b, c), (a + 1, b, c), (a, b - 1, c), (a, b + 1, c), (a, b, c - 1), (a, b, c + 1)):
            if i in existing:
                total -= 2
        existing.add((a, b, c))

print(total)