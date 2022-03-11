'''
Write a function, island_count, that takes in a grid containing Ws and Ls. 
W represents water and L represents land. 
The function should return the number of islands on the grid. 
An island is a vertically or horizontally connected region of land.

test_00:
grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

island_count(grid) # -> 3
'''

def island_count(grid):
    visited = set()
    count = 0 

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if explore(grid, row, col, visited):
                count += 1
    return count 

def explore(grid, r, c, visited):
    if not bounds(grid, r, c): return False 
    if grid[r][c] == 'W' : return False 
    pos = (r,c)
    if pos in visited: return False 
    visited.add(pos)
    
    explore(grid, r+1, c, visited)
    explore(grid, r-1, c, visited)
    explore(grid, r, c+1, visited)
    explore(grid, r, c-1, visited)
    return True

def bounds(grid, r, c):
    rowbound = 0 <= r < len(grid)
    colbound = 0 <= c < len(grid[0])
    return rowbound and colbound

grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(island_count(grid)) # -> 4

'''
Time Complexity : O (r*c)
Space Complexity: O (r*c)
'''