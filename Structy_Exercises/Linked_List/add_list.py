'''
Write a function, add_lists, that takes in the head of two linked lists, each representing a number. 
The nodes of the linked lists contain digits as values. The nodes in the input lists are reversed; 
this means that the least significant digit of the number is the head. 
The function should return the head of a new linked listed representing the sum of the input lists. 
The output list should have its digits reversed as well.

Say we wanted to compute 621 + 354 normally. The sum is 975:

   621
 + 354
 -----
   975

Then, the reversed linked list format of this problem would appear as:

    1 -> 2 -> 6
 +  4 -> 5 -> 3
 --------------
    5 -> 7 -> 9
test_00:
#   621
# + 354
# -----
#   975

a1 = Node(1)
a2 = Node(2)
a3 = Node(6)
a1.next = a2
a2.next = a3
# 1 -> 2 -> 6

b1 = Node(4)
b2 = Node(5)
b3 = Node(3)
b1.next = b2
b2.next = b3
# 4 -> 5 -> 3

add_lists(a1, b1)
# 5 -> 7 -> 9
test_01:
#  7541
# +  32
# -----
#  7573

a1 = Node(1)
a2 = Node(4)
a3 = Node(5)
a4 = Node(7)
a1.next = a2
a2.next = a3
a3.next = a4
# 1 -> 4 -> 5 -> 7

b1 = Node(2)
b2 = Node(3)
b1.next = b2
# 2 -> 3 

add_lists(a1, b1)
# 3 -> 7 -> 5 -> 7
'''
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def add_lists(head_1, head_2):
    dummy = Node(None)
    tail = dummy 

    current_1 = head_1
    current_2 = head_2
    carry = 0
    while current_1 or current_2 or carry == 1:
        val1 = 0 if not current_1 else current_1.val
        val2 = 0 if not current_2 else current_2.val

        total = val1 + val2 + carry 
        carry = 1 if total > 9 else 0
        digit = total % 10

        tail.next = Node(digit)
        tail = tail.next 
    
        if current_1: current_1 = current_1.next
        if current_2: current_2 = current_2.next
    return dummy.next 


    '''
    m: list 1 length
    n: list 2 length
    Time Complexity: O(max(m,n))
    Space Complexity: O(max(m,n))
    '''