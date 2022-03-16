'''
Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. 
The function should return the number of connected components within the graph.

test_00:
connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 2
test_01:
connected_components_count({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) # -> 1
'''

def connected_components_count(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore(graph,node, visited):
            count += 1
    return count 

def explore(graph, current, visited):
    if current in visited: return False
    visited.add(current)
    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
    return True

print(connected_components_count({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
})) # -> 1
print(connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 2

'''
n: number of nodes
e: number of edges
Time Complexity: O(e)
Space Complexity: O(n)
'''