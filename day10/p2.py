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


line=[]
for idx, el in enumerate(arr):
    xp, yp = idx%40, idx//40
    if(abs(el%40 -xp) <=1):
        line.append("#")
    else:
        line.append(".")
for i in range(6):
    print(line[40*i:40*(i+1)])
