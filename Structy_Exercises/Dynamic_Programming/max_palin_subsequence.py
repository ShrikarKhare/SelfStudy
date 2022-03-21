'''
Write a function, max_palin_subsequence, that takes in a string as an argument. 
The function should return the length of the longest subsequence of the string that is also a palindrome.

A subsequence of a string can be created by deleting any characters of the string, while maintaining the relative order of characters.

test_00:
max_palin_subsequence("luwxult") # -> 5
test_01:
max_palin_subsequence("xyzaxxzy") # -> 6
'''

def max_palin_subsequence(string):
    return _max_palin_subsequence(string, 0, len(string)-1, {})

def _max_palin_subsequence(string, i, j, memo):
    key = (i,j)
    if key in memo: return memo[key]
    if i == j: return 1
    if i > j: return 0

    if string[i] == string[j] :
        memo[key] = 2 + _max_palin_subsequence(string, i+1, j-1, memo)
    else:
        memo[key] = max(_max_palin_subsequence(string,i+1, j, memo),_max_palin_subsequence(string,i, j-1, memo))
    
    return memo[key]

print(max_palin_subsequence("xyzaxxzy"))

'''
n: len of string
Time Complexity: O(n^2)
Space Complexity: O(n^2)
'''