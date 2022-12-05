arrs = [[] for i in range(9)]
with open("input.txt") as f:
    for row in f:
        if not row.startswith("move"):
            for i in range(len(row)//4):
                ltr = row[i*4+1]
                if ltr != " " and ltr not in ("1230456789"):
                    arrs[i].insert(0,ltr)
        else:
            parts = row.strip().split()
            print(parts)
            ctr, frm, to = (int(parts[1]), int(parts[3])-1, int(parts[5])-1)
            while ctr > 0 and len(arrs[frm]) > 0:
                a = arrs[frm][len(arrs[frm])-1]
                del arrs[frm][len(arrs[frm])-1]
                arrs[to].append(a)
                ctr -= 1
for arr in arrs:
    print(arr[-1], end="")

