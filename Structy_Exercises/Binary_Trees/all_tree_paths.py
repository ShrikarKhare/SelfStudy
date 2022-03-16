'''
Write a function, all_tree_paths, that takes in the root of a binary tree. 
The function should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.

The order within an individual path must start at the root and end at the leaf, 
but the relative order among paths in the outer list does not matter.

You may assume that the input tree is non-empty.

test_00:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

all_tree_paths(a) # ->
# [ 
#   [ 'a', 'b', 'd' ], 
#   [ 'a', 'b', 'e' ], 
#   [ 'a', 'c', 'f' ] 
# ] 
test_01:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
f.left = i

#         a
#      /    \
#     b      c
#   /  \      \
#  d    e      f
#      / \    /   
#     g  h   i 

all_tree_paths(a) # ->
# [ 
#   [ 'a', 'b', 'd' ], 
#   [ 'a', 'b', 'e', 'g' ], 
#   [ 'a', 'b', 'e', 'h' ], 
#   [ 'a', 'c', 'f', 'i' ] 
# ] 
'''
class Node:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None 

def all_tree_paths(root):
    result = _all_tree_paths(root)
    for i in result:
        i[:] = i[::-1]
    return result 

def _all_tree_paths(root):
    if not root: return []
    if not root.left and not root.right: return [[root.val]]

    paths = []
    left = _all_tree_paths(root.left)
    right = _all_tree_paths(root.right)

    for i in left:
        i.append(root.val)
        paths.append(i)
    for i in right:
        i.append(root.val)
        paths.append(i)
    return paths

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
f.left = i

print(all_tree_paths(a))

'''
n: number of nodes
Time Complexity : O(n)
Space Complexity : O(n)
'''