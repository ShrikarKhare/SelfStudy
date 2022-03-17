'''
Write a function, max_path_sum, that takes in a grid as an argument. 
The function should return the maximum sum possible by traveling a path from the top-left corner to the bottom-right corner. 
You may only travel through the grid by moving down or right.

You can assume that all numbers are non-negative.

test_00:
grid = [
  [1, 3, 12],
  [5, 1, 1],
  [3, 6, 1],
]
max_path_sum(grid) # -> 18
test_01:
grid = [
  [1, 2, 8,  1],
  [3, 1, 12, 10],
  [4, 0, 6,  3],
]
max_path_sum(grid) # -> 36
'''

def max_path_sum(grid):
    return _max_path_sum(grid, 0, 0, {})

def _max_path_sum(grid, r, c, memo):
    if not bounds(grid, r, c): return float('-inf')
    if bottom_right(grid,r,c): return grid[r][c]
    pos = (r,c)
    if pos in memo: return memo[pos]

    down = _max_path_sum(grid,r+1, c, memo)
    right = _max_path_sum(grid,r, c+1, memo)

    memo[pos] = grid[r][c] + max(down,right)
    return memo[pos]

def bounds(grid,r,c):
    rowbound = 0 <= r < len(grid)
    colbound = 0 <= c < len(grid[0])
    return rowbound and colbound 
def bottom_right(grid,r,c):
    return r == len(grid)-1 and c == len(grid[0])-1

grid = [
  [1, 3, 12],
  [5, 1, 1],
  [3, 6, 1],
]

print(max_path_sum(grid)) # -> 18

grid = [
  [1, 2, 8,  1],
  [3, 1, 12, 10],
  [4, 0, 6,  3],
]

print(max_path_sum(grid)) # -> 36

'''
r: rows
c: columns
Time Complexity: O(r*c)
Space Complexity: O(r*c)
'''