def tandem_repeats(T):
    map = depth_first_numbering(T)
    inv_map = {v : k for k, v in map.items()}
    branching = []

    for node in T.root.children.values():
        __tandem_repeats(node, string_depth(node.index), T.x, branching, map, inv_map)
    
    non_branching = []
    
    # claim: left-rotation of branching tandem repeat only give rise to non-branching
    for t in branching:
        while True:
            start = t[0] - 1
            end = t[0] + t[1] - 1 
            if start >= 0 and T.x[start] == T.x[end]: # check if tandem repeat to the left
                t = (start, t[1], t[2])
                non_branching.append(t)
            else:
                break

    return (branching, non_branching)

def string_depth(t):
    return t[1] - t[0] + 1

def __tandem_repeats(root, depth, S, result, map, inv_map):
    if not root.children:
        return

    large_leaf_list = None
    for ch in root.children:
        child = root.children.get(ch)
        if large_leaf_list == None or abs(large_leaf_list[0] - large_leaf_list[1]) < abs(child.range[0] - child.range[1]):
          large_leaf_list = child.range
        __tandem_repeats(child, depth + string_depth(child.index), S, result, map, inv_map)
    
    range_lower = (root.range[0], large_leaf_list[0]) # lower partition of small
    range_upper = (large_leaf_list[1] + 1, root.range[1] + 1) # upper partition of small

    search_range(root, depth, S, result, range_lower, large_leaf_list, map, inv_map)
    search_range(root, depth, S, result, range_upper, large_leaf_list, map, inv_map)

def search_range(root, depth, S, result, partition, large_leaf_list, map, inv_map):
    for k in range(partition[0], partition[1]):
        i = map[k]
        j = inv_map.get(i + depth) # check if j is in leaf-list of v
        if j != None and (root.range[0] <= j and j <= root.range[1]):
            end = i + 2 * depth
            if end < len(S) and S[i] != S[end]:
                result.append((i, depth, 2))
        j = inv_map.get(i - depth) # check if j is in leaf-list of large(v)
        if j != None and (large_leaf_list[0] <= j and j <= large_leaf_list[1]):
            end = i + depth
            if S[i - depth] != S[end]:
                result.append((i - depth, depth, 2))

def depth_first_numbering(T):
    map = {} # map from positions to depth-first numbers
    __depth_first_numbering(T.root, 0, map)
    return map

def __depth_first_numbering(root, i, map):
    if not root.children:
        root.range = [i, i]
        map[i] = root.pos
        return i + 1
    root.range = [None, None]
    for ch in root.children:
        child = root.children.get(ch)
        i = __depth_first_numbering(child, i, map)
        if root.range[0] == None or root.range[0] > child.range[0]:
            root.range[0] = child.range[0] # min
        if root.range[1] == None or root.range[1] < child.range[1]:
            root.range[1] = child.range[1] # max
    return i