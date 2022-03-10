'''
Write a function, linked_list_find, that takes in the head of a linked list and a target value. 
The function should return a boolean indicating whether or not the linked list contains the target.
test_00:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linkedListFind(a, "c") # True
test_01:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linkedListFind(a, "d") # True
'''

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linkedListFind(head, target):
    current = head 
    while current:
        if current.val == target:
            return True
        current = current.next
    return False
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linkedListFind(a, "d"))

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''