'''
Write a function, most_frequent_char, that takes in a string as an argument. 
The function should return the most frequent character of the string. 
If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty.

test_00:
most_frequent_char('bookeeper') # -> 'e'
test_01:
most_frequent_char('david') # -> 'd'
'''
from collections import Counter
def most_freq_char(s):
    counter = Counter(s)
    most_frequent = None
    for char in s:
        if most_frequent is None or counter[most_frequent] < counter[char]:
            most_frequent = char 
    return most_frequent

print(most_freq_char('bookeeper'))

'''
Time Complexity: O(n)
Space Complexity: O(n)
'''