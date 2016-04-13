from collections import deque
import sys

class SuffixTree:
    def __init__(self, x): 
        self.x = x # client is assumed to append special char to end of x
        self.root = Node(None, None) # root of the suffix tree
        self.construct()

    def construct(self):
        for i in range(len(self.x)): # insert suffix x[i..n-1] for i = 0...n-1
            self.insert(i, i, self.root) 

    def insert(self, i, pos, node):
        first_ch = self.x[i]
        child = node.children.get(first_ch) # get child of current node with label starting with first_ch
        if child == None: # if no such child exist, insert new child of current node with label x[i..n-1]
            new_leaf = Node((i, len(self.x) - 1), pos)
            node.children[first_ch] = new_leaf # put child in dictionary with key first_ch
            return new_leaf
        j = 1 # offset into x[i..n-1] (x[i..n-1] and label of child match at first position)
        for ch in self.x[child.index[0] + 1:child.index[1] + 1]: # no suffix is a prefix of another, so i + j < n
            if not ch == self.x[i + j]: # mismatch: insert new node with children current node and child
                new_leaf = Node((i + j, len(self.x) - 1), pos)
                new_node = Node((child.index[0], child.index[0] + j - 1), pos)
                new_node.children[ch] = child
                new_node.children[self.x[i + j]] = new_leaf 
                child.index = (child.index[0] + j, child.index[1])
                node.children[first_ch] = new_node # set new child for first_ch
                return new_leaf
            else:
                j = j + 1 # update index to next ch
        return self.insert(i + j, pos, child) # child's label exhausted: recursively call insert()

class Node:
     def __init__(self, index, pos):
        self.index = index
        self.pos = pos
        self.children = {}      
    


def main():
   # if not len(sys.argv) == 2:
   #     sys.exit("Usage: ./search file pattern")

   # file = open(sys.argv[0], "r")
   # str = file.read()

   # pattern = sys.argv[1]

    x = "AABABABAABBAB"
    pattern = "A"
    T = SuffixTree(x + "$")
    exact_match(T, pattern)
    
def exact_match(T, pattern):
    return __exact_match(T.root, T.x, pattern)

def __exact_match(root, x, pattern):
    first_ch = pattern[0] 
    child = root.children.get(first_ch)
    
    if child == None:
        return False     

    j = 1
    for ch in pattern[1:]:
        if child.index[0] + j > child.index[1]:
            return __exact_match(child, x, pattern[j:])
        if not ch == x[child.index[0] + j]:
            return False
        j = j + 1
    
    bfs_print_match(child)
    return True 
      
def bfs_print_match(root):
    queue = deque([root])
    while queue:
        node = queue.pop()
        if node.index[1] == 13: # fix this
            print("Match at position: ", node.pos)
        for ch in sorted(node.children):
            queue.appendleft(node.children[ch])

def bfs_print_tree(root):
    queue = deque([root])
    while queue:
        node = queue.pop()
        print(node.index, "has children: ")
        for ch in sorted(node.children):
            print(ch, node.children[ch].children, node.children[ch].index)
            queue.appendleft(node.children[ch])

if __name__ == '__main__':
    main()