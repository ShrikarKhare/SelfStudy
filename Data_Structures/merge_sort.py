#Divide and Conquer/ Merge sort
def merge_sort(list):
    '''
    sort the given list in an ascending order
    returns a new sorted list

    Divide: find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Overall takes (k n log n) time
    '''

    if len(list) <= 1:
        return list
    
    def split(list):
        '''
        Divide the unsorted list at midpoint into sublsts
        Returns two sublists, left and right

        Takes overall of O(k log n)
        '''
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:] 

        return left,right
    left_half , right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    def merge(left,right):
        '''
        Merges two lists, sorting them in the process
        Returns a new merged list
        
        Runs in overall O(n) time
        '''
        l =[]
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                l.append(left[i])
                i+=1
            else:
                l.append(right[j])
                j+=1
        while i < len(left):
            l.append(left[i])
            i+=1

        while j < len(right):
            l.append(right[j])
            j+=1

        return l

    return merge(left,right)

alist = [1,5,2,6,31,25,237,10]
l = merge_sort(alist)
# print(l)
def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True 
    
    return list[0] < list[1] and verify_sorted(list[1:])
print(verify_sorted(alist))
print(verify_sorted(l))