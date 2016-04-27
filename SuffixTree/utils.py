import string
import random

def gen_rand_str(size=10, chars=string.ascii_uppercase):
    return "".join(random.choice(chars) for _ in range(size))

def bfs_print_tree(root):
    queue = deque([root])
    while queue:
        node = queue.pop()
        print(node.index, "has children: ")
        for ch in sorted(node.children):
            print(ch, node.children[ch].children, node.children[ch].index)
            queue.appendleft(node.children[ch])
