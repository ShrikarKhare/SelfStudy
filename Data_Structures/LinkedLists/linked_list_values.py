class Node:
    val = None
    next = None

    def __init__(self, val):
        self.val = val

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b 
b.next = c
c.next = d 

#  a-> b-> c-> d-> None
#                  curr 

# def print_Linked_list(head):
#     current = head 
#     while current != None:
#         print(current.val)
#         current = current.next

def print_Linked_list(head):
    if head == None: return
    print(head.val)
    print_Linked_list(head.next)

    current = head 

#  a-> b-> c-> d-> None
#                  head 
# print_Linked_list(a)

'''returns all the values in a linked List'''
def linked_list_values(head):
    current = head
    values = []
    while current is not None:
        values.append(current.val)
        current = current.next
    return values


def linked_list_values(head):
    values =[]
    fillValues(head, values)
    return values 

def fillValues(head,values):
    if head == None: return
    values.append(head.val)
    fillValues(head.next, values)

# print_Linked_list(a)

# def sumList(head):
#     ans = 0
#     current = head
#     while current is not None:
#         ans += current.val
#         current = current.next 
#     return ans

#recursive
# def sumList(head):
#     if head is None: return 0
#     return head.val +sumList(head.next)    
#iterative
# def linked_list_find(head, target):
#     current = head
#     while current is not None:
#         if current.val == target:
#             return True
#         current = current.next
#     return False
#recursive
# def linked_list_find(head,target):
#     if head is None: return False
#     if head.val is target: return True
#     return linked_list_find(head.next, target)

#recursive
def get_node_value(head, index):
    if head is None: return None 
    if index is 0: return head.val
    return get_node_value(head.next, index-1)

#iterative
def get_node_value(head,index):
    if head is None: return None 
    current = head 
    count = 0
    while current is not None:
        current = current.next 
        count+=1 
        if count == index:
            return current.val
    return None

#iterative
def reverse_list(head):
    prev = None 
    curr = head 
    while curr is not None:
        temp = curr.next 
        curr.next = prev 
        prev = curr 
        curr = temp 
    return prev 
#recursion
def reverse_list(head , prev = None):
    if head is None: return prev 
    next = head.next 
    head.next = prev 
    return reverse_list(next, head)

#iterative    
# def zipper_lists(head1, head2):
#     tail = head1
#     curr1 = head1.next
#     curr2 = head2
#     count = 0

#     while curr1 and curr2:

#         if count %2 == 0:
#             tail.next == curr2 
#             curr2 = curr2.next 
#         else:
#             tail.next == curr1 
#             curr1 = curr1.next 
#         tail = tail.next 

#         count+=1
    
#     if curr1 is not None:
#         tail.next = curr1
#     if curr2 is not None:
#         tail.next = curr2

#recursive

def zipper_lists(head1,head2):
    if head1 is None and head2 is None: return None 
    if head1 is None: return head2 
    if head2 is None: return head1 
    temp1 = head1.next 
    temp2 = head2.next
    head1.next = head2
    # head2.next = temp
    
    head2.next = zipper_lists(temp1,temp2)
    return head1