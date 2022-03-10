'''
Write a function `allConstruct(target,wordBank)` that accepts a 
target string and an array of strings

The function should return a 2D array containing all the ways 
that the target can be constructed by concatenating elements of 
the wordBank array. Each element of the 2D array should represent 
one combination that constructs the target

You may reuse elements of `wordBank` as many times as needed
'''
def allConstruct(target, wordBank, memo = None):
    if memo is None:
        memo ={}
    if target in memo: return memo[target]
    if target == '': return [[]]
    result = []
    for i in wordBank:
        if target.startswith(i):
            suffix = target[len(i):]
            suffixWays = allConstruct(suffix, wordBank,memo)
            targetways = map(lambda x: [i, *x],suffixWays)
            result.extend(targetways)
    memo[target] = result
    return result

'''
m = len(target)
n = len(wordBank)

Brute Force 
Time: O(n^m)
Space: O(m)

Memoized
Time: O(n^m)
Space: O(m)
'''
print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) #2
print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'])) #1
print(allConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) #0
# print(allConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) #4
print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) #0