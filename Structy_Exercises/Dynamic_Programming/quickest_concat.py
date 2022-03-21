'''
Write a function, quickest_concat, that takes in a string and a list of words as arguments. 
The function should return the minimum number of words needed to build the string by concatenating words of the list.

You may use words of the list as many times as needed.

test_00:
quickest_concat('caution', ['ca', 'ion', 'caut', 'ut']) # -> 2
test_01:
quickest_concat('caution', ['ion', 'caut', 'caution']) # -> 1
'''

def quickest_concat(s, words):
    ans = _quickest_concat(s,words,{})
    if ans == float('inf'):
        return -1
    return ans 

def _quickest_concat(s,words,memo):
    if s in memo: return memo[s]
    if s == '': return 0

    min_words = float('inf')

    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            current = 1 + _quickest_concat(suffix, words,memo)
            min_words = min(min_words,current)
    memo[s] = min_words
    return memo[s]

'''
s: len of string
w: len of words
Time Complexity: O(sw)
Space Complexity: O(s)
'''