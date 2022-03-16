'''
Write a function, level_averages, that takes in the root of a binary tree that contains number values. 
The function should return a list containing the average value of each level.

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

level_averages(a) # -> [ 3, 7.5, 1 ] 
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

level_averages(a) # -> [ 5, 32.5, 17.5, 2 ] 
'''

from collections import deque
from statistics import mean  
def level_averages(root): 
    queue = deque([(root,0)])
    result = [] 
    averages = []
    
    while queue:
        current, lvl = queue.popleft()
        if len(result) == lvl:
            result.append([current.val])
        else:
            result[lvl].append(current.val)
        if current.left:
            queue.append((current.left, lvl+1))
        if current.right:
            queue.append((current.right, lvl+1))
    for i in result:
        averages.append(mean(i))
    return averages

class Node: 
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None
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

print(level_averages(a))