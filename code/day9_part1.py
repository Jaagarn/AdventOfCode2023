import sys

sys.setrecursionlimit(30)

class Node:
    def __init__(self, own, left, right):
        self.own = own
        self.left = left
        self.right = right
    def __str__(self) -> str:
        if(self.left is None):
            return f"Node: {self.own}, left: None, right: None"
        else:
            return f"Node: {self.own}, left: {self.left.own}, right: {self.right.own}"

def build_first_roots(input_roots):
    new_roots = []
    for root in input_roots:
        new_roots.append(Node(own= int(root), left= None, right= None))
    return new_roots

def build_tree(input_tree):
    list_tree = [node.own for node in input_tree]
    print(list_tree)
    set_input = set(list_tree)
    if((len(set_input) == 1 and 0 in set_input)):
        return input_tree
    new_tree = []
    for i in range(len(input_tree)-1):
        left, right = int(input_tree[i].own), int(input_tree[i+1].own)
        own = left - right
        new_tree.append(Node(own= own, left= input_tree[i], right= input_tree[i+1]))

    return build_tree(new_tree)

if len(sys.argv) != 2:
    raise ValueError('Please provide path to the data.')

print(f'Path is {sys.argv[1]}')
path = sys.argv[1]

with open(path, 'r', encoding="utf-8") as f:
    lines = f.read().splitlines()

trees = [build_tree(build_first_roots(list(reversed(line.split())))) for line in lines]

final_value = 0

for tree in trees:
    last_root = tree[0]
    node = last_root.left
    new_value = 0
    while (True):
        if(node.left is None):
            new_value += node.own
            break
        else:
            new_value += node.own
            node = node.left
    final_value += new_value

print(final_value)