'''
Write a function `bestSum(targetSum, numbers)` that takes in a 
targetSum and an array of numbers as arguments

The function should return an array containing the shortest 
combination of numbers that add up to exactly the targetSum

If there is a tie for the shortest combination, you may return any 
one of the shortest
'''
def bestSum(targetSum, numbers, memo = None):
    if memo is None:
        memo = {}

    if targetSum in memo: return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None 
    
    bestcombination = None
    for i in numbers: 
        remainder = targetSum - i 
        remainderCombination = bestSum(remainder, numbers, memo)
        if remainderCombination is not None:
            combination = [*remainderCombination , i]
            if bestcombination is None or ( len(combination) < len(bestcombination)):
                bestcombination = combination
        
    memo[targetSum] = bestcombination
    return bestcombination

# m = target sum
# n = numbers.length

#Brute Force
# time complexity : O(n^m*m)
# space complexity : O(m^2)

#Memoized 
# time complexity: O(m^2 * n)
# space complexity: O(m^2)

print(bestSum(7, [5,3,4,7]))
print(bestSum(8, [2,3,5]))
print(bestSum(8, [1,4,5]))
print(bestSum(100, [1,2,5,25]))