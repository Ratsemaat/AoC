from collections import defaultdict

def get_priority(ltr):
    if ord(ltr)>96:
        return ord(ltr) - 96
    else:
        return ord(ltr)-38

def get_priority_sums_of_common_ltrs(a, b):
    dict_a = defaultdict(lambda: 0)
    dict_b = defaultdict(lambda: 0)
    for char_a in a:
        curr = dict_a[char_a]
        dict_a[char_a] = curr+1

    for char_b in b:
        curr = dict_b[char_b]
        dict_b[char_b] = curr + 1

    total = 0
    for char in dict_a.keys():
        val_a = dict_a.get(char, 0)
        val_b = dict_b.get(char, 0)
        if min(val_a, val_b)>0:
            total += get_priority(char) #* min(val_a, val_b)//
    print(total)
    return total

def get_priority_sums_of_common_ltrs(rows):
    start = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for row in rows:
        string = set(row)
        start=start.intersection(string)

    for el in start:
        return get_priority(el)

with open("input.txt") as f:
    data = [l.strip() for l in f.readlines()]

def partA():
    total = 0
    for row in data:
        mid = len(row) // 2
        start = row[:mid]
        end = row[mid:]
        total += get_priority_sums_of_common_ltrs(start,end)
    return total

def partB():
    total = 0
    for i in range(0, len(data), 3):
        rows = [data[i], data[i+1], data[i+2]]
        total += get_priority_sums_of_common_ltrs(rows)
    return total
print(partB())