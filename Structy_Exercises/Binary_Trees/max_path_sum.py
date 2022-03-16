'''
Write a function, max_path_sum, that takes in the root of a binary tree that contains number values. 
The function should return the maximum sum of any root to leaf path within the tree.

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

max_path_sum(a) # -> 18
test_01:
a = Node(5)
b = Node(11)
c = Node(54)
d = Node(20)
e = Node(15)
f = Node(1)
g = Node(3)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g

#        5
#     /    \
#    11    54
#  /   \      
# 20   15
#      / \
#     1  3

max_path_sum(a) # -> 59
'''

def max_path_sum(root):
    if not root: return float('-inf')
    if not root.left and not root.right: return root.val
    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))

class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 

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

print(max_path_sum(a))

'''
n: number of nodes
Time Complexity: O(n)
Space Complexity: O(n)
'''