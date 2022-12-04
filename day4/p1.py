with open("input.txt") as f:
    data = [l.strip() for l in f.readlines()]

ctr=0

for row in data:
    parts = row.split(",")
    a = parts[0].split("-")
    b = parts[1].split("-")

    if int(a[0])<=int(b[0]) and int(a[1])>=int(b[1]) or int(b[0])<=int(a[0]) and int(b[1])>=int(a[1]):
        ctr+=1

    """ 
    part b
     if int(a[0])<=int(b[1]) and int(a[0])>= int(b[0]) or int(b[0])<=int(a[1]) and int(b[0])>= int(a[0]) :
        ctr+=1
    """
print(ctr)