from suffix_tree import *
from utils import gen_rand_str
import time

def exact_match(T, pattern):
    return __exact_match(T.root, T.x, pattern)

def __exact_match(root, x, pattern): # exact match algorithm
    first_ch = pattern[0] 
    child = root.children.get(first_ch)
    
    if child == None:
        return []     

    j = 1
    for ch in pattern[1:]:
        if child.index[0] + j > child.index[1]:
            return __exact_match(child, x, pattern[j:])
        if not ch == x[child.index[0] + j]:
            return []
        j = j + 1
    
    return bfs_match(child)
      
def bfs_match(root):
    positions = []
    queue = deque([root])
    while queue:
        node = queue.pop()
        if not node.children:
            positions.append(node.pos)
        for ch in node.children:
            queue.appendleft(node.children[ch])
    return positions

def main():
    x_len = 100000
    p_len = 25
    print("|x| =", x_len, "|p| =", p_len, flush=True)
    x = gen_rand_str(x_len, chars="AB")
    total = 0

    t = time.process_time()
    T = suffix_tree(x + "$")
    elapsed_time = time.process_time() - t
    total += elapsed_time
    print("construct =", elapsed_time, "total =", total, flush=True)
    
    for i in range(10):
        p = gen_rand_str(p_len, chars="AB")
        t = time.process_time()
        matches = exact_match(T, p)
        elapsed_time = time.process_time() - t
        total += elapsed_time
        print("round =", elapsed_time, "total =", total, flush=True)


if __name__ == '__main__':
    main()