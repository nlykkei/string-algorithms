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