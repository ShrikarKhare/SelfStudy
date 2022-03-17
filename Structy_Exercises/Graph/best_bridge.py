'''
Write a function, best_bridge, that takes in a grid as an argument. 
The grid contains water (W) and land (L). 
There are exactly two islands in the grid. 
An island is a vertically or horizontally connected region of land. 
Return the minimum length bridge needed to connect the two islands. A bridge does not need to form a straight line.

test_00:
grid = [
  ["W", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "L"],
  ["L", "L", "L", "W", "L"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
]
best_bridge(grid) # -> 1
test_01:
grid = [
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["L", "L", "W", "W", "L"],
  ["W", "L", "W", "W", "L"],
  ["W", "W", "W", "L", "L"],
  ["W", "W", "W", "W", "W"],
]
best_bridge(grid) # -> 2
'''
from collections import deque
def best_bridge(grid):

  main_island = None 
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      potential_island = explore(grid, row, col, set())
      if len(potential_island) > 0 :
        main_island = potential_island
        break
  visited = set(main_island)
  queue = deque([])

  for each in main_island:
    r, c = each
    queue.append((r,c, 0))

  while queue:
    r, c, distance = queue.popleft()
    if grid[r][c] == 'L' and (r,c) not in visited:
      return distance - 1
    
    deltas = [(0,1), (0,-1), (1,0), (-1,0)]

    for delta in deltas: 
      dr, dc = delta 
      nr,nc = dr+r, dc+c 
      n_pos = (nr,nc)

      if bounds(grid,nr,nc) and n_pos not in visited:
        queue.append((nr,nc,distance+1))
  return -1 
 

def explore(grid, r, c, visited):
  if not bounds(grid, r, c): return visited
  if grid[r][c] == 'W': return visited
  pos = (r,c)
  if pos in visited: return visited 
  visited.add(pos)
  
  explore(grid, r-1, c, visited)
  explore(grid, r+1, c, visited)
  explore(grid, r, c-1, visited)
  explore(grid, r, c+1, visited)

  return visited

def bounds(grid,r,c):
  rowbound = 0 <= r < len(grid)
  colbound = 0 <= c < len(grid[0])
  return rowbound and colbound

grid = [
  ["W", "L", "W", "W", "W", "W", "W", "W"],
  ["W", "L", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "L", "W"],
  ["W", "W", "W", "W", "W", "W", "L", "L"],
  ["W", "W", "W", "W", "W", "W", "W", "L"],
]
print(best_bridge(grid)) # -> 8


'''
r : number of rows
c : number of columns
Time Complexity: O(r*c)
Space Complexity: O(r*c)
'''