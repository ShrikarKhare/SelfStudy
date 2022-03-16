'''
Write a function, tree_value_count, that takes in the root of a binary tree and a target value. 
The function should return the number of times that the target occurs in the tree.

test_00:
a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12

tree_value_count(a,  6) # -> 3
'''
#DFS
def tree_value_count(root,target):
    stack = [root]
    count = 0
    while stack:
        current = stack.pop()
        if current.val == target:
            count += 1
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return count
#BFS
from collections import deque
def tree_value_count(root, target):
    queue = deque([root])
    count = 0
    while queue:
        current = queue.popleft()
        if current.val == target:
            count += 1
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return count
#recursive
# def tree_value_count(root, target):
#     if not root: return 0
#     count = 1 if root.val == target else 0
#     return count + tree_value_count(root.left,target) + tree_value_count(root.right,target)



class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 

a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(tree_value_count(a,6))

'''
n: number of nodes
Time Complexity: O(n)
Space Complexity: O(n)
'''