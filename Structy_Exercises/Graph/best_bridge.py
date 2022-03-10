from collections import deque
def best_bridge(grid):
  main_island = None
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      island = traverse(grid,r,c,set())
      if len(island) > 0:
        main_island = island
        break
  visited = set(main_island)
  queue = deque([])
  for pos in main_island:
    r,c = pos
    queue.append((r,c,0))
  
  while queue:
    row,col,dist = queue.popleft()
    if grid[row][col] == 'L' and (row,col) not in main_island:
      return dist-1
    
    deltas = [(1,0), (-1,0), (0,1), (0,-1)]
    for delta in deltas:
      dr, dc = delta
      nr, nc = dr+row, dc+col
      n_pos = (nr,nc)
      
      if bounds(grid,nr,nc) and n_pos not in visited:
        visited.add(n_pos)
        queue.append((nr,nc,dist+1))
        
def bounds(grid,r,c):
  row_bound = 0 <= r < len(grid)
  col_bound = 0 <= c < len(grid[0])
  return row_bound and col_bound

def traverse(grid,r,c,visited):
  pos = (r,c)
  if pos in visited or not bounds(grid,r,c) or grid[r][c] =='W' : return visited
  visited.add(pos)
  
  deltas = [(1,0), (-1,0), (0,1), (0,-1)]
  for delta in deltas:
    dr, dc = delta
    nr, nc = dr+r, dc+c
    traverse(grid,nr,nc,visited)
  return visited