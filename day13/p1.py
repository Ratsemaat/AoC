from copy import deepcopy

EX = "ex.txt"
IN = "input.txt"
with open(EX) as f:
    grid = f.readlines()

pairs = []
for i in range(len(grid) // 3 + 1):
    pairs.append((grid[i * 3].strip(), grid[i * 3 + 1].strip()))


def parse(string):
    lst = []
    lvl = 0
    stack = ""
    for char in string:

        if char == "[":
            if lvl > 0:
                stack += char
            lvl += 1
            continue

        if lvl == 1 and char == ",":
            lst.append(stack)
            stack = ""
            continue

        if char == "]":
            lvl -= 1
            if lvl > 1:
                stack += "]"
            elif lvl == 1:
                stack += "]"
                stack = parse(stack)
            else:
                lst.append(stack)
            continue

        else:
            stack += char

    return lst


total = 0


def compare(ls, rs):
    li, ri = 0, 0
    while True:
        if li >= len(ls) and ri >= len(rs):
            return None
        elif li >= len(ls) :
            return True
        elif ri >= len(rs):
            return False

        le, re = ls[li], rs[ri]
        print(le, re)
        if re == "" or le == "":
            if le != "": return False
            if re != "": return True

        elif type(re) != list and type(le) != list:
            if int(re) != int(le):
                return int(re) > int(le)
        else:
            if type(le) != list:
                le = [le]

            if type(re) != list:
                re = [re]

            val = compare(le, re)
            if val is not None:
                return val
        li += 1
        ri += 1


total = []
for idx, (l, r) in enumerate(pairs):
    print(idx + 1)
    ls = parse(l)
    rs = parse(r)
    val = compare(ls, rs)
    if val:
        print(idx + 1, "IN")
        total.append(idx + 1)

print(total)
print(sum(total))
