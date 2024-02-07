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

root = monkis["root"]


def solve(eq):
    if eq.isnumeric():
        return int(eq)
    else:

        a, sign, b = eq.split()
        match sign:
            case "+":
                return solve(monkis[a])+solve(monkis[b])
            case "-":
                return solve(monkis[a])-solve(monkis[b])
            case "*":
                return solve(monkis[a])*solve(monkis[b])
            case "/":
                return solve(monkis[a])/solve(monkis[b])

print(solve(root))