'''
Write a function, path_finder, that takes in the root of a binary tree and a target value. 
The function should return an array representing a path to the target value. 
If the target value is not found in the tree, then return None.

You may assume that the tree contains unique values.

test_00:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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

path_finder(a, 'e') # -> [ 'a', 'b', 'e' ]
test_01:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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

path_finder(a, 'p') # -> None
'''

class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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

def path_finder(root, target):
    result = _path_finder(root, target)
    if result == None: return None 
    return result[::-1]

def _path_finder(root, target):
    if not root: return None 
    if root.val == target: return [root.val]

    left = _path_finder(root.left, target)
    right = _path_finder(root.right, target)

    if left:
        left.append(root.val)
        return left 
    if right:
        right.append(root.val)
        return right
    return None 

print(path_finder(a, 'e')) # -> [ 'a', 'b', 'e' ]

'''
Time Complexity: O(n)
Space Complexity: O(n)
'''