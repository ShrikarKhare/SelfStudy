'''
Write a function, is_univalue_list, that takes in the head of a linked list as an argument. 
The function should return a boolean indicating whether or not the linked list contains exactly one unique value.

You may assume that the input list is non-empty.

test_00:
a = Node(7)
b = Node(7)
c = Node(7)

a.next = b
b.next = c

# 7 -> 7 -> 7

is_univalue_list(a) # True
test_01:
a = Node(7)
b = Node(7)
c = Node(4)

a.next = b
b.next = c

# 7 -> 7 -> 4

is_univalue_list(a) # False
'''
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def is_univalue_list(head):
    current = head
    while current:
        if current.val != head.val:
            return False
        current = current.next
    return True 

a = Node(7)
b = Node(7)
c = Node(4)

a.next = b
b.next = c

# 7 -> 7 -> 4

is_univalue_list(a) # False

'''
Time Complexity: O(n)
Space Complexity: O(1)

'''