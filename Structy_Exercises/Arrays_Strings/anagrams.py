'''
Write a function, anagrams, that takes in two strings as arguments. 
The function should return a boolean indicating whether or not the strings are anagrams. 
Anagrams are strings that contain the same characters, but in any order.
test_00:
anagrams('restful', 'fluster') # -> True
test_01:
anagrams('cats', 'tocs') # -> False
'''
# #Python solution
# from collections import Counter
# def anagrams(s1, s2):
#     return Counter(s1) == Counter(s2)

#regular solution
def anagrams(s1,s2):
    return char_count(s1) == char_count(s2)

def char_count(s):
    count = {}
    for i in s:
        if i not in count:
            count[i] = 0
        count[i] += 1
    return count


print(anagrams('restful', 'fluster'))

'''
n : string1 length
m : string2 length
Time Complexity: O(n + m)
Space Complexity: O(n + m)
'''