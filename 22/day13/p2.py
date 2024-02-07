from functools import cmp_to_key


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




EX = "ex.txt"
IN = "input.txt"
with open(IN) as f:
    grid = f.readlines()

all=[]
for i in range(len(grid) // 3 + 1):
    all.append(parse(grid[i * 3].strip()))
    all.append(parse(grid[i * 3 + 1].strip()))

a = parse("[[2]]")
b = parse("[[6]]")
all.append(a)
all.append(b)

print(compare(all[2], all[3]))
print(all)
all.sort(key=cmp_to_key(lambda x,y: 1 if compare(x, y) else -1), reverse=True)
print((all.index(b)+1) * (all.index(a)+1))
print(all)
