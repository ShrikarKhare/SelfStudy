'''
Write a function, closest_carrot, that takes in a grid, a starting row, and a starting column. 
In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots. 
The function should return a number representing the length of the shortest path from the starting position to a carrot. 
You may move up, down, left, or right, but cannot pass through walls (X). 
If there is no possible path to a carrot, then return -1.

test_00:
grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

closest_carrot(grid, 1, 2) # -> 4
test_01:
grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

closest_carrot(grid, 0, 0) # -> 5
'''
from collections import deque
def closest_carrot(grid, starting_row, starting_col):
    visited = set((starting_row, starting_col))
    queue = deque([(starting_row,starting_col, 0)])

    while queue:
        r, c, distance = queue.popleft()
        if grid[r][c] == 'C':
            return distance 
        
        deltas = [(0,1),(0,-1), (1,0),(-1,0)]
        for delta in deltas:
            dr, dc = delta 
            nr, nc = dr+r, dc+c 
            pos = (nr,nc)

            if bounds(grid,nr,nc) and pos not in visited and grid[r][c] != 'X':
                visited.add(pos)
                queue.append((nr,nc, distance+1))
    return -1

def bounds(grid,r,c):
    rowbound = 0 <= r < len(grid)
    colbound = 0 <= c < len(grid[0])
    return rowbound and colbound


grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

print(closest_carrot(grid, 1, 2)) # -> 5


'''
r : number of rows
c : number of columns
Time Complexity: O(r*c)
Space Complexity: O(r*c)
'''