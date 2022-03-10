'''
    Depth first traversal
    uses a stack data structure


    breadth first traversal
    uses a queue data structure
'''

# def depthfirstPrint(graph, source):
#     stack = [ source ]

#     while len(stack) > 0:
#         current = stack.pop()
#         print(current)
#         for i in graph[current]:
#             stack.append(i)
        

# graph = {
#     'a' : ['b','c'],
#     'b' : ['d'],
#     'c' : ['e'],
#     'd' : ['f'],
#     'e' : [],
#     'f' : []
# }             


#Recursive
# def depthfirstPrint(graph, source):
#     print(source)
#     for i in graph[source]:
#         depthfirstPrint(graph, i)    

# depthfirstPrint(graph,'a')

# def breadthfirstPrint(graph, source):
#     queue = [ source ]
    
#     while len(queue) > 0:
#         current = queue.pop(0)
#         print(current)
#         for i in graph[current]:
#             queue.append(i)
# breadthfirstPrint(graph,'a')

from typing import Set


# graph = {
#     'f': ['g','i'],
#     'g': ['h'],
#     'h': [],
#     'i': ['g','k'],
#     'j': ['i'],
#     'k': [],

# }
# def has_path(graph, source, destination):
#     if source == destination: return True 
#     for i in graph[source]:
#         if has_path(graph, i, destination) == True:
#             return True
#     return False 


# def has_path(graph,source,destination):
#     queue = [ source ]
#     while len(queue) > 0:
#         current = queue.pop(0)
#         if current == destination:
#             return True 
#         for i in graph[current]:
#             queue.append(i)
#     return False
# print(has_path(graph, 'f', 'h'))
# print(has_path(graph, 'h', 'j'))
 
# def buildGraph(edges):
#     graph = {}
#     for edge in edges:
#         [a,b] = edge
#         if a not in graph:
#             graph[a] = []
#         if b not in graph:
#             graph[b] = []
#         graph[a].append(b)
#         graph[b].append(a)
#     return graph 

# edges = [
#     ['i','j'],
#     ['k','i'],
#     ['m','k'],
#     ['k','l'],
#     ['o','n']
# ]

# def has_path(graph, source, destination, visited = None):
#     if visited is None:
#         visited = set()
#     if source in visited: return False
#     if source == destination: return True
#     visited.add(source) 
#     for i in graph[source]:
#         if has_path(graph, i, destination, visited) == True:
#             return True 
#     return False
# def undirectedPath(edges,nodeA, nodeB):
#     graph = buildGraph(edges)
#     return has_path(graph, nodeA,nodeB)
    
# print(undirectedPath(edges, 'j','m'))

# def connectedComponentsCount(graph):
#     visited = set()
#     count = 0
#     for i in graph:
#         if explore(graph, i , visited) == True:
#             count+=1
#     return count

# def explore(graph, current, visited):
#     if current in visited: return False
#     visited.add(current)
#     for i in graph[current]:
#         explore(graph, i, visited)
#     return True

 
# graph = {
#     0: [8,1,5],
#     1: [0],
#     5: [0,8],
#     8: [0,5],
#     2: [3,4],
#     3: [2,4],
#     4: [3,2],
# }
# print(connectedComponentsCount(graph))

# def largest_component(graph):
#     visited = set() 
#     largest = 0
#     for i in graph:
#         current = explore(graph, i, visited)
#         if current > largest: largest = current
#     return largest

# def explore(graph, node, visited):
#     if node in visited: return 0
#     visited.add(node)
#     size = 1
#     for i in graph[node]:
#         size += explore(graph,i,visited)
    
#     return size

# print(largest_component(graph))

# edges = [
#     ['w','x'],
#     ['x','y'],
#     ['z','y'],
#     ['z','v'],
#     ['w','v']
# ]

# def build_graph(edges):
#     graph = {}
#     for edge in edges:
#         [ nodeA, nodeB ] = edge
#         if not (nodeA in graph): graph[nodeA] = []
#         if not (nodeB in graph): graph[nodeB] = []
#         graph[nodeA].append(nodeB)
#         graph[nodeB].append(nodeA)
#     return graph

# def shortest_path(edges, nodeA,nodeB):
#     graph = build_graph(edges)
#     queue = [ [nodeA, 0] ]
#     visited = set([nodeA, 0]) 
#     print(graph)

#     while len(queue) > 0:
#         [current, distance] = queue.pop(0)
#         for i in graph[current]:
#             queue.append([i, distance+1])
#             if not i in visited:
#                 visited.add(i)
#         if current == nodeB:
#             return distance 
#     return -1
# print(shortest_path(edges, 'w','z'))

# grid = [ 
#     ['W', 'L', 'W', 'W', 'W'],
#     ['W', 'L', 'W', 'W', 'W'],
#     ['W', 'W', 'W', 'L', 'W'],
#     ['W', 'W', 'L', 'L', 'W'],
#     ['L', 'W', 'W', 'L', 'L'],
#     ['L', 'L', 'W', 'W', 'W']
# ]
# def island_count(grid):
#     visited = set()
#     count = 0
#     for row in range(len(grid)):
#         for col in range(len(grid[0])):
#             if explore(grid, row,col, visited) == True:
#                 count+=1
#     return count

# def explore(grid, row, col, visited):
#     rowInbounds = 0 <= row and row < len(grid)
#     colInbounds = 0 <= col and col < len(grid[0])

#     if not rowInbounds or not colInbounds: return False
#     if grid[row][col] == "W": return False
#     position = str(row) + '.' + str(col)
#     if position in visited: return False 
#     visited.add(position)

#     explore(grid, row -1, col, visited)
#     explore(grid, row +1, col, visited)
#     explore(grid, row, col-1, visited)
#     explore(grid, row, col+1, visited)

#     return True

# print(island_count(grid))

grid = [ 
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W']
]

def min_island(grid):
    visited = set()
    minsize = float('inf')
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            current = exploreSize(grid,row,col,visited)
            if current < minsize and current > 0:
                minsize = current
    return minsize

def exploreSize(grid, row, col, visited):
    rowInbounds = 0 <= row and row < len(grid)
    colInbounds = 0 <= col and col < len(grid[0])

    if not rowInbounds or not colInbounds: return 0
    if grid[row][col] == 'W': return 0

    position = str(row)+','+str(col)
    
    if position in visited: return 0
    
    visited.add(position)

    size = 1
    size += exploreSize(grid, row-1 ,col, visited) + exploreSize(grid, row+1 ,col, visited) + exploreSize(grid, row , col-1, visited)+ exploreSize(grid, row , col+1, visited)
    return size

print(min_island(grid))