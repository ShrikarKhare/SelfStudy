'''
Write a function min_change that takes in an amount and a list of coins. 
The function should return the minimum number of coins required to create the amount. 
You may use each coin as many times as necessary.

If it is not possible to create the amount, then return -1.

test_00:
min_change(8, [1, 5, 4, 12]) # -> 2, because 4+4 is the minimum coins possible
test_01:
min_change(13, [1, 9, 5, 14, 30]) # -> 5
test_02:
min_change(23, [2, 5, 7]) # -> 4
'''
def min_change(amount, coins):
    result = _min_change(amount, coins, {})
    if result == float('inf'): return -1 
    return result 

def  _min_change(amount, coins, memo):
    if amount in memo: return memo[amount]
    if amount == 0 : return 0
    if amount < 0 : return float('inf')

    smallest = float('inf')

    for coin in coins:
        current = 1 + _min_change(amount-coin, coins, memo)
        smallest = min(smallest,current)
    memo[amount] = smallest 
    return memo[amount]

print(min_change(13, [1, 9, 5, 14, 30]))


'''
Time Complexity: O(n)
Space Complexity: O(n)
'''