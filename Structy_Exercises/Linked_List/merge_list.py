'''
Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments. 
The function should merge the two lists together into single sorted linked list. 
The function should return the head of the merged linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty and contain increasing sorted numbers.

test_00:
a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(6)
r = Node(8)
s = Node(9)
t = Node(25)
q.next = r
r.next = s
s.next = t
# 6 -> 8 -> 9 -> 25

merge_lists(a, q)
# 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28 
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None 

def merge_list(head_1, head_2):
    dummy = Node(None)
    tail = dummy 
    current_head1 = head_1
    current_head2 = head_2
    while current_head1 and current_head2:
        if current_head1.val < current_head2.val:
            tail.next = current_head1
            current_head1 = current_head1.next
        else:
            tail.next = current_head2
            current_head2 = current_head2.next
        tail = tail.next 
    if current_head1 is not None: tail.next = current_head1
    if current_head2 is not None: tail.next = current_head2
    return dummy.next

a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(6)
r = Node(8)
s = Node(9)
t = Node(25)
q.next = r
r.next = s
s.next = t
# 6 -> 8 -> 9 -> 25

print(merge_list(a, q))
# 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28 

'''
Time Complexity: O(min(n , m))
Space Complexity: O(1)

'''