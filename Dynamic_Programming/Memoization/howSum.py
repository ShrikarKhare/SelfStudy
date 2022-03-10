'''
Write a function `howSum(targetSum, numbers)` that takes in a 
targetSum and an array of numbers as arguments.

The function should return an array containing any combination of
elements that add up to exactly the targetSum, then return null.

If there are multiple combinations possible, you may return any single one
'''
def howSum(targetSum, numbers, memo = None):
    if memo is None:
        memo = {}
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0 : return []
    if targetSum < 0 : return None
    for num in numbers:
        remainder = targetSum - num 
        remainderResult = howSum(remainder, numbers, memo)
        if(remainderResult != None):
            memo[targetSum] = [*remainderResult , num]
            return memo[targetSum]
    memo[targetSum] = None
    return memo[targetSum]

# def howSum(targetSum, numbers, memo = None):
#     if memo is None:
#         memo ={}
#     if targetSum == 0 :
#         return []
#     if targetSum < 0 :
#         return None
#     if targetSum in memo: return memo[targetSum]

#     for num in numbers:
#         remainder = targetSum - num 
#         remainderResult = howSum(remainder, numbers, memo)
#         if(remainderResult != None):
#             memo[targetSum] = [*remainderResult , num]
#             return memo[targetSum]
#     memo[targetSum] = None
#     return None


print(howSum(7,[2,3])) #T
print(howSum(7,[5,3,4,7])) #T
print(howSum(7,[2,4])) #F
print(howSum(8,[2,3,5])) #T
print(howSum(300,[7,14])) #F