'''
Write a function, can_concat, that takes in a string and a list of words as arguments. 
The function should return boolean indicating whether or not it is possible to concatenate words of the list 
together to form the string.

You may reuse words of the list as many times as needed.

test_00:
can_concat("oneisnone", ["one", "none", "is"]) #  -> True
test_01:
can_concat("oneisnone", ["on", "e", "is"]) #  -> False
'''
def can_concat(s, words):
    return _can_concat(s, words, {})

def _can_concat(s, words, memo):
    if s in memo: return memo[s]
    if s == '': return True 

    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            if _can_concat(suffix, words, memo):
                memo[s] = True 
                return memo[s]
    memo[s] = False
    return memo[s] 

'''
s: len of string
w: number of words
Time Complexity: O(sw)
Space Complexity: O(s)
'''
