'''
Write a function, minimum_island, that takes in a grid containing Ws and Ls. 
W represents water and L represents land. 
The function should return the size of the smallest island. 
An island is a vertically or horizontally connected region of land.

You may assume that the grid contains at least one island.

test_00:
grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

minimum_island(grid) # -> 2
test_01:
grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

minimum_island(grid) # -> 1
'''
def minimum_island(grid):
    visited = set()
    smallest = float('inf')

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            current = explore(grid, row, col, visited)
            if current > 0 :
                smallest = min(current, smallest)
    return smallest

def explore(grid, r, c, visited):
    if not bounds(grid,r,c): return 0
    if grid[r][c] == 'W' : return 0
    pos = (r,c)
    if pos in visited: return 0 
    visited.add(pos)

    size = 1 

    return size + ( 
        explore(grid, r-1, c, visited)+
        explore(grid, r+1, c, visited)+
        explore(grid, r, c+1, visited)+
        explore(grid, r, c-1, visited)
        )


def bounds(grid, r, c):
    rowbound = 0 <= r < len(grid)
    colbound = 0 <= c < len(grid[0])
    return rowbound and colbound

grid = [
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(minimum_island(grid))