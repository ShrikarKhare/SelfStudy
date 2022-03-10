'''
Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.

test_00:
intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
test_01:
intersection([2,4,6], [4,2]) # -> [2,4]
'''
def intersection(list1, list2):
    visited = set(list1)
    result = []
    for i in list2:
        if i in visited:
            result.append(i)
    return result 

print(intersection([4,2,1,6], [3,6,9,2,10]))

'''
n: length of list1
m: length of list2
Time Complexity: O(n+m)
Space Complexity: O(n)
'''