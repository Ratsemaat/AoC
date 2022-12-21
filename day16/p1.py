import re

EX = "ex.txt"
IN = "input.txt"

grid = [["." for i in range(1000)] for j in range(1000)]

with open(EX) as f:
    data = [row.strip() for row in f]

pairs = []
mp=[[31 for i in range(len(data))]for j in range(len(data))]
print(mp)
for idx,row in enumerate(data):
    z = re.match("Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? (.+)", row)
    pl, rate, neigh = (z.groups())
    mp.append([])
    print(rate)



