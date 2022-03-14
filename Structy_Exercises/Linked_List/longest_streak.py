'''
Write a function, longest_streak, that takes in the head of a linked list as an argument. 
The function should return the length of the longest consecutive streak of the same value within the list.

test_00:
a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 5 -> 5 -> 7 -> 7 -> 7 -> 6

longest_streak(a) # 3
test_01:
a = Node(3)
b = Node(3)
c = Node(3)
d = Node(3)
e = Node(9)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 3 -> 3 -> 3 -> 3 -> 9 -> 9

longest_streak(a) # 4
'''
def longest_streak(head):
    current_streak = 0
    longest_streak = 0
    current = head 
    prev = None 

    while current: 
        if current.val == prev: 
            current_streak += 1
        else:
            current_streak = 1
        
        current_streak = max(current_streak,longest_streak)
        prev = current.val
        current = current.next
    return longest_streak

    '''
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''