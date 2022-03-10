from linked_list import LinkedList

def merge_sort(linkedlist):
    '''
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeated merge the sublists to produce sorted sublists until one remains
    Returns a sorted linked list

    '''

    if linkedlist.size() == 1:
        return linkedlist
    elif linkedlist.head == None:
        return linkedlist

    left_half, right_half = split(linkedlist)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)
def split(linkedlist):
    '''
    Divide the unsorted list at midpoint into sublists

    '''
    if linkedlist.head == None or linkedlist == None:
        left_half = linkedlist
        right_half = None 
        return left_half , right_half
    else:
        size = linkedlist.size()
        mid = size //2
        mid_node = linkedlist.node_at_index(mid-1)
        left_half = linkedlist
        right_half = LinkedList()
        right_half.head = mid_node.next_node 
        mid_node.next_node = None

        return left_half, right_half
def merge(left,right):
    '''
    merges two linked lists, sorting by data in the nodes
    returns a new merged list

    '''
    #Create a new linked list that contains nodes from merging left and right

    merged = LinkedList()
    
    #Add a fake head that is discarded later
    merged.add(0)

    #set current to the head of the linekd list
    current = merged.head
    #obtain head nodes for left and right linekd lists
    left_head = left.head
    right_head = right.head

    #iterate over left and right until we reach the tail node of either
    while left_head or right_head:
        #if the head node of left is None, we're past the tail
        #add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            #call next on right to set loop condition to false
            right_head = right_head.next_node
        #if the head node of left is None, we're past the tail
        #add the node from right to merged linked list
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            #If left data is < right set current to left node
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
            #If right data is < left set current to right node
                current.next_node = right_head
                right_head = right_head.next_node
        current = current.next_node

    #Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head 

    return merged
l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)
print(l)

sorted_linked_list = merge_sort(l)
print(sorted_linked_list)