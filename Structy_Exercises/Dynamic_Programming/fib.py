'''
Write a function fib that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.

The 0-th number of the sequence is 0.

The 1-st number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous two numbers.

Solve this recursively.
'''
def fib(n, memo = {}):
    if n < 2: return n 
    if n in memo: return memo[n]
    memo[n] =  fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(0)); # -> 0
print(fib(100))

'''
Time Complexity: O(n)
Space Complexity: O(n)
'''