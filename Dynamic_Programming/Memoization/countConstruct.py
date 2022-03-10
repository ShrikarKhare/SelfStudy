'''
Write a function `countConstruct(target, wordBank)` that accepts a 
target string and an array of strings.

The function should return the number of ways that the `target` can 
be constrcuted by concatentating elements of the `wordBank` array.

You may reuse elements of `wordBank` as many times as needed.
'''
def countConstruct(target, wordBank, memo = None):
    if memo is None:
        memo = {}

    if target == "": return 1
    if target in memo: return memo[target]
    count = 0
    for i in wordBank:
        if target.startswith(i):
            suffix = target[len(i):]
            numways = countConstruct(suffix,wordBank, memo)
            count+= numways

    memo[target] = count
    return memo[target]

'''
m = target.length
n = wordBank.length

Brute Force
Time: O(n^m *m)
Space O(m^2)

Memoized
Time: O(n*m^2)
Space: O(m^2)
'''
print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) #2
print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) #1
print(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) #0
print(countConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) #4
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) #0