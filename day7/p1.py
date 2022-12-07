from treelib import Node, Tree

tree = Tree()
tree.create_node("root", "/")
current=""

map={}

with open("input.txt") as f:
    for line in f:
        parts = line.split()
        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "..":
                    current = "/".join(current.split("/")[:-2])+"/"
                elif parts[2].startswith("/"):
                    current = parts[2]
                else:
                    current += (parts[2]+"/")
        elif parts[0] == "dir":
            dir = current+parts[1]+"/"
            tree.create_node(dir, dir, parent=current)
        else:
            for i in range(1,len(current.split("/"))):
                dir = "/".join(current.split("/")[:i]) + "/"
                if dir not in map:
                    map[dir] = 0
                map[dir] += int(parts[0])

    print(map)
total=0
for el in sorted(map.items()):
    #print(el)
    if el[1]>=3837783:
        print(el)
