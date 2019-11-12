from collections import deque
import sys
import time
from suffix_tree_match import exact_match
from utils import gen_rand_str

class suffix_tree:
    def __init__(self, x): 
        self.x = x # client is assumed to append special char to end of x
        self.root = suffix_node(None, None, None, None) # root of the suffix tree
        self.naive_construct()

    def naive_construct(self): # O(n^2) time bound construction
        for i in range(len(self.x)): # insert suffix x[i..n-1] for i = 0...n-1
            self.insert(i, i, self.root) 

    def insert(self, i, pos, node):
        first_ch = self.x[i]
        child = node.children.get(first_ch) # get child of current node with label starting with first_ch
        if child == None: # if no such child exist, insert new child of current node with label
                          # x[i..n-1]
            new_leaf = suffix_node((i, len(self.x) - 1), pos, node, None)
            node.children[first_ch] = new_leaf # put child in dictionary with key first_ch
            return new_leaf
        j = 1 # offset into x[i..n-1] (x[i..n-1] and label of child match at first position)
        for ch in self.x[child.index[0] + 1:child.index[1] + 1]: # no suffix is a prefix of another, so i + j < n
            if not ch == self.x[i + j]: # mismatch: insert new node with children current node and child
                new_node = suffix_node((child.index[0], child.index[0] + j - 1), pos , node, None)
                new_leaf = suffix_node((i + j, len(self.x) - 1), pos, new_node, None)
                new_node.children[ch] = child
                new_node.children[self.x[i + j]] = new_leaf 
                child.index = (child.index[0] + j, child.index[1])
                child.parent = new_node
                node.children[first_ch] = new_node # set new child for first_ch
                return new_leaf
            else:
                j = j + 1 # update index to next ch
        return self.insert(i + j, pos, child) # child's label exhausted: recursively call insert()

class suffix_node:
     def __init__(self, index, pos, parent, s):
        self.index = index # characters on edge from parent to this node
        self.pos = pos # starting position in x
        self.children = {} # children of this node
        self.parent = parent # parent of this node
        self.suffix_link = s # suffix link

def main():
    if not len(sys.argv) == 3:
        sys.exit("Usage: ./search file pattern")

    file = open(sys.argv[1], "r")
    x = file.read()

    pattern = sys.argv[2]

    print(gen_rand_str(100))

    # time suffix tree construction
    t = time.process_time()
    T = suffix_tree(x + "$") # construct suffix tree
    elapsed_time = time.process_time() - t

    print("Suffix tree construction:", elapsed_time, "seconds.")

    # time exact match algorithm
    t = time.process_time()
    positions = exact_match(T, pattern) # exact match for pattern
    elapsed_time = time.process_time() - t
    print("Exact match:", elapsed_time, "seconds.")

    if not positions:
        print("No matches found")
    else:
        print("Matches found: ", end="")
        for i in sorted(positions):
            print(i + 1, end=" ")
    print()

if __name__ == '__main__':
    main()