class Node:

    data = None
    next_node = None

    def __init__(self,data):
        self.data = data 

class LinkedList:
    def __init__(self):
        self.head = None
    

def middleNode(self, head):
    end = head 
    while end and end.next:
        head = head.next 
        end = end.next.next
    return head

