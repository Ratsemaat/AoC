map = []
with open("input.txt") as f:
    for line in f:
        row = (list(line.strip()))
        map.append(row)

max = 0


def calculate_scenic_score(map, i, j):
    left, right, up, down = 0, 0, 0, 0
    h = int(map[i][j])
    orig_i = i
    orig_j = j

    while j > 0:
        if int(map[i][j - 1]) < h:
            left += 1
            j -= 1
        else:
            left += 1
            break

    j = orig_j
    while j < (len(map[0]) - 1):
        if int(map[i][j + 1]) < h:
            right += 1
            j += 1
        else:
            right += 1
            break
    j = orig_j

    while i > 0:
        if int(map[i - 1][j]) < h:
            down += 1
            i -= 1
        else:
            down += 1
            break
    i = orig_i

    while i < (len(map) - 1):
        if int(map[i + 1][j]) < h:
            up += 1
            i += 1
        else:
            up += 1
            break
    print(up, down, left, right)
    return up * down * left * right


for i in range(1, len(map) - 1):
    for j in range(1, len(map[0]) - 1):
        val = calculate_scenic_score(map, i, j)
        if val > max:
            max = val

print(max)
