'''
Write a function, count_paths, that takes in a grid as an argument. 
In the grid, 'X' represents walls and 'O' represents open spaces. 
You may only move down or to the right and cannot pass through walls. 
The function should return the number of ways possible to travel from the top-left corner of the grid to the bottom-right corner.

test_00:
grid = [
  ["O", "O"],
  ["O", "O"],
]
count_paths(grid) # -> 2
test_01:
grid = [
  ["O", "O", "X"],
  ["O", "O", "O"],
  ["O", "O", "O"],
]
count_paths(grid) # -> 5
'''

def count_paths(grid):
    return _count_paths(grid, 0, 0, {})

def bounds(grid,r,c):
    rowbound = 0 <= r < len(grid)
    colbound = 0 <= c < len(grid[0])
    return rowbound and colbound

def bottom_right(grid,r,c):
    return r == len(grid)-1 and c == len(grid[0])-1

def _count_paths(grid, r, c, memo):
    if not bounds(grid,r,c) or grid[r][c] == 'X': return 0
    if bottom_right(grid,r,c): return 1
    pos = (r,c)
    if pos in memo: return memo[pos]

    left = _count_paths(grid, r, c+1, memo)
    down = _count_paths(grid, r+1, c, memo)

    memo[pos] = left + down 
    return memo[pos]

grid = [
  ["O", "O", "X"],
  ["O", "O", "O"],
  ["O", "O", "O"],
]
print(count_paths(grid))

'''
Time Complexity: O(r*c)
Space Complexity: O(r*c)
'''