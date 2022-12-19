EX = "ex.txt"
IN = "input.txt"

grid = [["." for i in range(1000)] for j in range(1000)]

with open(IN) as f:
    data = [row.strip() for row in f]

pairs = []
for row in data:
    parts = row.split(":")
    x1, y1 = int(parts[0][12:].split(",")[0]), int(parts[0].split("=")[2])
    x2, y2 = int(parts[1][24:].split(",")[0]), int(parts[1].split("=")[2])
    pairs.append(((x1, y1), (x2, y2)))

occupied = set()

row_ranges = []


class Range:
    MIN = 0
    MAX = 0

    def __init__(self, MIN, MAX):
        self.MIN = MIN
        self.MAX = MAX

    def __eq__(self, other):
        try:
            return self.MIN == other.MIN and self.MAX == other.MAX
        except AttributeError:
            return False

    def __hash__(self):
        return hash(self.MIN) + hash(self.MAX)

    def __repr__(self):
        return "min: " + str(self.MIN) + ", max:" + str(self.MAX)


class Node:
    right = None
    left = None
    rng = None

    def __init__(self, rng, left, right):
        self.rng = rng
        self.left = left
        self.right = right


class RangeTree:
    root = None

    def __repr__(self):
        return self.get_bracket_form(self.root)

    def insert(self, range):

        if not self.root:
            self.root = Node(range, None, None)
            return

        self.insert_helper(self.root, range)

    def get_range_count(self, node):
        if not node:
            return 0
        return self.get_range_count(node.left) + 1 + self.get_range_count(node.right)

    def get_bracket_form(self, node):
        if not node:
            return ""
        return self.get_bracket_form(node.left) + str(node.rng) + self.get_bracket_form(node.right)

    def insert_helper(self, node, range):
        if range.MAX < node.rng.MIN-1:
            if node.left:
                return self.insert_helper(node.left, range)
            node.left = Node(range, None, None)
        else:
            node.rng.MIN = min(range.MIN, node.rng.MIN)

        if range.MIN > node.rng.MAX+1:
            if node.right:
                return self.insert_helper(node.right, range)
            node.right = Node(range, None, None)
        else:
            node.rng.MAX = max(range.MAX, node.rng.MAX)

        node.rng.MAX = self.prune_smaller(node.right, node.rng.MAX, node)
        node.rng.MIN = self.prune_bigger(node.left, node.rng.MIN, node)

    def prune_smaller(self, node, value, par):
        if not node:
            return value
        if node.rng.MIN > 1 + value:
            if node.left:
                return self.prune_smaller(node.left, value, par)
            return value
        if node.rng.MAX > 1 + value:
            par.right = node.right
            return node.rng.MAX
        else:
            if node.right:
                par.right = node.right
                return self.prune_smaller(node.right, value, par)
            else:
                par.right = None
                return value

    def prune_bigger(self, node, value, par):
        if not node:
            return value
        if node.rng.MAX < value - 1:
            if node.right:
                return self.prune_bigger(node.right, value, par)
            return value
        if node.rng.MIN < value - 1:
            par.left=node.left
            return node.rng.MIN
        else:
            if node.left:
                par.left = node.left
                return self.prune_bigger(node.left, value, par)
            else:
                par.left = None
                return value


for row in range(4000000):
    print(row)
    rt = RangeTree()
    for pair in pairs:
        dist = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
        sx, sy = pair[0]
        if dist > abs(row - sy):
            diff = dist - abs(row - sy)
            rt.insert(Range(sx - diff, sx + diff))
    if rt.get_range_count(rt.root) > 1:
        print(rt, row)
        break

occupied.difference_update(set([pair[0] for pair in pairs]))
occupied.difference_update(set([pair[1] for pair in pairs]))

print(len(occupied))
