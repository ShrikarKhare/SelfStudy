'''
Write a function `canSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments.

The function should return a boolean indicating whether or not it 
is possible to generate the targetSum using numbers from the array

You may use an element of the array as many times as needed.
You may assume that all input numbers are nonnegative.
'''
def canSum(targetSum, nums, memo = None):
    if memo is None:
        memo = {}
    key = targetSum
    if key in memo: return memo[key]
    if targetSum == 0: return True 
    if targetSum < 0: return False 

    for i in nums:
        remainder = targetSum - i 
        if(canSum(remainder, nums, memo) == True):
            memo[key] = True
            return True
    memo[key] = False 
    return False

print(canSum(7,[2,3])) #T
print(canSum(7,[5,3,4,7])) #T
print(canSum(7,[2,4])) #F
print(canSum(8,[2,3,5])) #T
print(canSum(300,[7,14])) #F