'''
Write a function, get_node_value, that takes in the head of a linked list and an index. 
The function should return the value of the linked list at the specified index.

If there is no node at the given index, then return None.

test_00:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

get_node_value(a, 2) # 'c'
test_01:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

get_node_value(a, 3) # 'd'
'''
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def get_node_value(head, idx):
    if not head: return None
    current = head 
    while current:
        if idx == 0: 
            return current.val
        current = current.next
        idx -= 1
    return None 

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

print(get_node_value(a, 3))

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''