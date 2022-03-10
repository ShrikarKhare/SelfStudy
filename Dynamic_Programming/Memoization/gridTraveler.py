'''
Say that you are a traveler on a 2D grid, You begin in the top-left corner and your goal is to
travel to the bottom-right corner. you may only move down or right

In how many ways can you travel to the goal on a grid with dimensions m * n ?

Write a function `gridTraveler(m, n)` that calculates this.
'''
def gridTraveler(m, n, memo ={}):
    key = (str(m) + ', ' + str(n))
    if key in memo: return memo[key]
    if m == 1 or n == 1: return 1
    if m == 0 or n == 0: return 0
    memo[key] = gridTraveler(m, n-1, memo) + gridTraveler(m-1,n, memo)
    return memo[key]
print(gridTraveler(1,1))
print(gridTraveler(2,3))
print(gridTraveler(3,2))
print(gridTraveler(3,3))
print(gridTraveler(18,18))
print(gridTraveler(42,3))
