EX = "ex.txt"
IN = "input.txt"
import re
from collections import defaultdict


with open(IN) as f:
    data = [row.strip() for row in f]

arr=[1,1]
for idx,row in enumerate(data):
    if row.startswith("addx"):
        arr.append(arr[-1]+int(row.split()[1]))
        arr.append(arr[-2]+int(row.split()[1]))
    else:
        arr.append(arr[-1])

