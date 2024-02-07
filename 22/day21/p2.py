import math

EX = "ex.txt"
IN = "input.txt"

grid = [["." for i in range(1000)] for j in range(1000)]

existing = set()
total = 0
monkis = {}

with open(IN) as f:
    # data=[8,2,32,-41,6,29,-4,6,-8,8,-3,-8,3,-5,0,-1,2,1,10,-9]
    data = [row.strip() for row in f]

for row in data:
    a, b = row.split(": ")
    monkis[a] = b

def toInt(str):
    try:
        int(str)
        return True
    except:
        return False

def solve(eq):
    if eq == "x":
        return "x"
    elif toInt(eq):
        return int(eq)
    else:
        a, sign, b = eq.split()
        sola = solve(monkis[a])
        solb = solve(monkis[b])
        match sign:
            case "+":
                if (type(sola) in (int, float) or sola.isnumeric()) and (
                        type(solb) in (int, float) or solb.isnumeric()):
                    return sola + solb
                else:
                    return "(" + str(sola) + "+" + str(solb) + ")"
            case "-":
                if (type(sola) in (int, float) or sola.isnumeric()) and (
                        type(solb) in (int, float) or solb.isnumeric()):
                    return sola - solb
                else:
                    return "(" + str(sola) + "-" + str(solb) + ")"
            case "*":
                if (type(sola) in (int, float) or sola.isnumeric()) and (
                        type(solb) in (int, float) or solb.isnumeric()):
                    return sola * solb
                else:
                    return "(" + str(sola) + "*" + str(solb) + ")"
            case "/":
                if (type(sola) in (int, float) or sola.isnumeric()) and (
                        type(solb) in (int, float) or solb.isnumeric()):
                    return sola / solb
                else:
                    return "(" + str(sola) + "/" + str(solb) + ")"


monkis["humn"] = "x"
root = monkis["root"]
print(root)
a, sign, b = root.split()
print(solve(monkis[a]), solve(monkis[b]))

num = 10**13
decrement =10**13
while True:
    print(num, decrement)
    monkis["humn"] = str(num)
    root = monkis["root"]
    a, sign, b = root.split()
    sola = solve(monkis[a])
    solb = solve(monkis[b])
    print(sola)
    print(solb)
    if solve(monkis[a]) == solve(monkis[b]):
        print(num)
        break
    elif sola > solb:
        num += decrement
        decrement=math.ceil(decrement / 2)
    elif sola < solb:
        num -= decrement
        decrement=math.ceil(decrement / 2)
