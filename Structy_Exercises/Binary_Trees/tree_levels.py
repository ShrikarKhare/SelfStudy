'''
Write a function, tree_levels, that takes in the root of a binary tree. 
The function should return a 2-Dimensional list where each sublist represents a level of the tree.

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

tree_levels(a) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
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

tree_levels(a) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f'],
#   ['g', 'h', 'i']
# ]
'''
from collections import deque
def tree_levels(root):

    queue = deque([(root, 0)])
    result = []

    while queue:
        current, lvl = queue.popleft()
        if len(result) == lvl:
            result.append([current.val])
        else:
            result[lvl].append(current.val)
        if current.left:
            queue.append([current.left, lvl+1])
        if current.right:
            queue.append([current.right, lvl+1])
    return result 

class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None
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

print(tree_levels(a))

'''
n : number of nodes
Time Complexity: O(n)
Space Complexity: O(n)
'''