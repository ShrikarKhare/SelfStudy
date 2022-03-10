'''
Write a function `fib(n)` that takes in a number as an argument. The function should return the n-th number of the 
Fibonnaci sequence

the 1st and 2nd number of the sequence is 1
to generate the next number of the sequence, we sum the previous two.
n :     1,2,3,4,5,6,7,8,9,10
fib(n): 1,1,2,3,5,8,13,21,34
'''

'''
memoization
 keys will be arg to the function, vale will be the return value
'''
def fib(n, memo = {}):
    if n in memo: return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2,memo)
    return memo[n]
print(fib(6)) #8
print(fib(7)) #13
print(fib(8)) #21
print(fib(50)) #812586269025 