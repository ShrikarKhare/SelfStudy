'''
Write a function `canConstruct(target, wordBank)` that accepts a 
target string and an array of strings.

The function should return a boolean indicating whether or not the 
`target` can be constructed by concatenating elements of the
`wordBank` array.

You may reuse elements of `wordBank` as many times as needed.
'''
def canConstruct(target, wordBank, memo = None):
    if memo is None:
        memo = {}

    if target == "" : return True
    if target in memo: return memo[target]
    
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):] 
            if canConstruct(suffix, wordBank,memo) == True:
                memo[target] = True
                return memo[target]
            
    memo[target] = False
    return memo[target]

'''
Brute Force
 m = len(target)
 n = len(wordBank)
 height of the tree is m 
 time Complexity :  O(n^m * m)
 space Complexity:  O(m^2)

Memoized
 m = len(target)
 n = len(wordBank)
 time Complexity: O (n * m^2)
 space Complexity: O (m^2)
'''

        
print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) #T
print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) #F
print(canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) #T
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) #F