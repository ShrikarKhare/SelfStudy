'''
Write a function sum_possible that takes in an amount and a list of positive numbers. 
The function should return a boolean indicating whether or not it is possible to create the amount by summing numbers of the list. 
You may reuse numbers of the list as many times as necessary.

You may assume that the target amount is non-negative.

test_00:
sum_possible(8, [5, 12, 4]) # -> True, 4 + 4
test_01:
sum_possible(15, [6, 2, 10, 19]) # -> False
'''
def sum_possible(amount, numbers):
    return _sum_possible(amount, numbers, {})

def _sum_possible(amount, numbers, memo):
    if amount == 0: return True 
    if amount < 0 : return False 
    if amount in memo: return memo[amount]

    for num in numbers:
        if _sum_possible(amount-num, numbers, memo):
            memo[amount] = True
            return memo[amount]
    memo[amount] = False 

    return memo[amount]

print(sum_possible(8, [5, 12, 4])) # -> True, 4 + 4
print(sum_possible(15, [6, 2, 10, 19])) # -> False) 

'''
a: amount
n: numbers
Time Complexity: O(a*c)
Space Complexity: O(a)
'''