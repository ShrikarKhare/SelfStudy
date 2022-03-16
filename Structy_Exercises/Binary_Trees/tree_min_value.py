'''
Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. 
The function should return the minimum value within the tree.

You may assume that the input tree is non-empty.

test_00:
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
tree_min_value(a) # -> -2
test_01:
a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(14)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       5
#    /    \
#   11     3
#  / \      \
# 4   14     12

tree_min_value(a) # -> 3
'''

#DFS
# def tree_min_value(root):
#     stack = [root]
#     min_value = float('inf')

#     while stack:
#         current = stack.pop()
#         min_value = min(min_value, current.val)

#         if current.left:
#             stack.append(current.left)
#         if current.right:
#             stack.append(current.right)
#     return min_value 

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None

a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(14)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


#BFS
from collections import deque
def tree_min_value(root):
    min_value = float('inf')
    queue = deque([root])

    while queue:
        current = queue.popleft()
        min_value = min(min_value, current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return min_value

#recursive
def tree_min_value(root):
    if not root: return float('inf')
    return min(root.val, tree_min_value(root.left), tree_min_value(root.right))
    
print(tree_min_value(a))
'''
n : number of nodes
Time Complexity: O(n)
Space Complexity: O(n)
'''