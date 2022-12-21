EX = "ex.txt"
IN = "input.txt"

grid = [["." for i in range(1000)] for j in range(1000)]

existing = set()
total = 0

with open(IN) as f:
    #data=[8,2,32,-41,6,29,-4,6,-8,8,-3,-8,3,-5,0,-1,2,1,10,-9]
    data = [811589153*int(row.strip()) for row in f]

dict = {}
for num in data:
    for ltr in "abcdefghijk":
        if str(num) + ltr not in dict:
            dict[str(num) + ltr] = num
            break
data = list(dict.keys())
orig_data = data.copy()
idx = 0


def rotate(data, num):
    loc = data.index(num)
    new_loc = (loc + dict[num]) %(len(data)-1)

    del data[loc]
    if new_loc == 0:
        data.append(num)
    else:
        data.insert(new_loc, num)
    return data


while True:
    idx += 1
    #print(data, orig_data[(idx - 1) % len(data)])
    data = rotate(data, orig_data[(idx - 1) % len(data)])
    if idx >= 10*len(data):
        print(data, orig_data[(idx - 1) % len(data)])

        a = (data[(data.index("0a") + 1000) % (len(data))])
        b = (data[(data.index("0a") + 2000) % (len(data))])
        c = (data[(data.index("0a") + 3000) % (len(data))])
        print(a, b, c)
        print(sum([dict[a], dict[b], dict[c]]))
        break
