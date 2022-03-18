'''
Write a function, summing_squares, that takes a target number as an argument. 
The function should return the minimum number of perfect squares that sum to the target. 
A perfect square is a number of the form (i*i) where i >= 1.

For example: 1, 4, 9, 16 are perfect squares, but 8 is not perfect square.

Given 12:

summing_squares(12) -> 3

The minimum squares required for 12 is three, by doing 4 + 4 + 4.

Another way to make 12 is 9 + 1 + 1 + 1, but that requires four perfect squares.
test_00:
summing_squares(8) # -> 2
test_01:
summing_squares(9) # -> 1
test_02:
summing_squares(12) # -> 3
'''
import math
def summing_squares(n):
    return _summing_squares(n, {})

def _summing_squares(n, memo):
    if n in memo: return memo[n]
    if n == 0 : return 0

    min_squares = float('inf')
    for i in range(1, math.floor(math.sqrt(n))+1):
        squares = i * i 
        current = 1 + _summing_squares(n-squares, memo)
        min_squares = min(current, min_squares)
    
    memo[n] = min_squares
    return memo[n]

print(summing_squares(8)) # -> 2
print(summing_squares(9)) # -> 1
print(summing_squares(12)) # -> 3

'''
n: length of nums
Time Complexity: O(n * sqrt(n))
Space Complexity: O(n)
'''