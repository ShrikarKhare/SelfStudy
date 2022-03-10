class Node:
    data = None
    left = None 
    right = None 

    def __init__(self,data):
        self.data = data
        

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c 
b.left = d 
b.right = e 
c.right = f 

#iterative version
# def depthFirstValues (root):
#     if root is None: return []
#     stack = [ root ]
#     result = []
#     while len(stack) > 0:
#         current = stack.pop()
#         result.append(current.data)
#         if current.right is not None: stack.append(current.right)
#         if current.left is not None: stack.append(current.left)
    
#     return result

#recursive version
# def depthFirstValue(root):
#     if root is None: return []
#     left = depthFirstValue(root.left)
#     right = depthFirstValue(root.right)
#     return [root.data, *left, *right]
# print(depthFirstValue(a))

#iterative, because recursion depends on call stacks, which is a bit unncessary when it comes to queues
def breadthFirstValue(root):
    if root is None: return []
    queue = [ root ]
    result = []

    while len(queue) > 0:
        current = queue.pop(0)
        result.append(current.data)
        if current.left is not None: queue.append(current.left)
        if current.right is not None: queue.append(current.right)
    return result 

# print(breadthFirstValue(a))

# def tree_includes(root, target):
#     if root is None: return False 
#     queue = [ root ]
#     while len(queue) > 0:
#         current = queue.pop(0)
            
#         if current.data == target:
#             return True
#         if current.left is not None: queue.append(current.left)
#         if current.right is not None: queue.append(current.right)
#     return False
# print(tree_includes(a, 'r'))

def tree_includes(root,target):
    if root is None: return False
    if root.data == target: return True
    return tree_includes(root.left,target) or tree_includes(root.right,target)

print(tree_includes(a, 'e'))
print(tree_includes(a, 'r'))
