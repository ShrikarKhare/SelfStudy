'''
Write a function, largest_component, that takes in the adjacency list of an undirected graph. 
The function should return the size of the largest connected component in the graph.

test_00:
largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 4
test_01:
largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) # -> 6
'''
def largest_component(graph):
    visited = set()
    largest = 0 
    for node in graph:
        current = explore(graph,node, visited)
        largest = max(largest,current)
    return largest

def explore(graph,node,visited):
    if node in visited: return 0
    visited.add(node)

    total = 1
    for neighbor in graph[node]:
        total += explore(graph,neighbor,visited)
    return total

print(
    largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) 
)# -> 6

print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}))# -> 4

'''
n: number of nodes
e: number of edges
Time Complexity: O(e)
Space Complexity: O(n)
'''