EX = "ex.txt"
IN = "input.txt"
import re
from collections import defaultdict

monki_funcs = []

with open(IN) as f:
    data = f.read()
    data = data.split("\n\n")

items = [[] for i in data]
#print(items)
dict = defaultdict(lambda: 0)
tot=1
for monki in data:
    tot *= int(re.findall('divisible by [0-9]+', monki)[0].split()[2])

print(tot)
for idx, monki in enumerate(data):
    parts = monki.split('\n')
    items[idx] = [int(el) for el in re.findall('[0-9]+', parts[1])]
    op = parts[2][19:]
    divisable_by = int(re.findall('[0-9]+', parts[3])[0])
    true_case = int(re.findall('[0-9]+', parts[4])[0])
    false_case = int(re.findall('[0-9]+', parts[5])[0])

    print(false_case, true_case)
    def func(old, true_case=true_case, false_case=false_case, divisable_by=divisable_by, op=op):
        op_parts = op.split()
        if op_parts[2] == "old":
            if op_parts[1] == "*":
                new = old * old
            else:
                new = old + old
        else:
            if op_parts[1] == "*":
                new = old * int(op_parts[2])
            else:
                new = old + int(op_parts[2])

        items[true_case].append(new % tot) if new % tot % divisable_by == 0 else items[false_case].append(
            new % tot)
    monki_funcs.append(func)

for i in range(10000):
    #print(items)
    for idx, monki_items in enumerate(items):
        for item in monki_items:
            dict[idx] += 1
            monki_funcs[idx](item)
        items[idx] = []

print(sorted(dict.values()))
print(sorted(dict.values())[-1]*sorted(dict.values())[-2])