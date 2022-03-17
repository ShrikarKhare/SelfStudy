'''
Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph. 
The function should return the length of the longest path within the graph. 
A path may start and end at any two nodes. 
The length of a path is considered the number of edges in the path, not the number of nodes.

test_00:
graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': []
}

longest_path(graph) # -> 2
test_01:
graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': [],
  'q': ['r'],
  'r': ['s', 'u', 't'],
  's': ['t'],
  't': ['u'],
  'u': []
}

longest_path(graph) # -> 4
'''

def longest_path(graph):
    distance = {}

    for node in graph:
        if len(graph[node]) == 0:
            distance[node] = 0
    for node in graph:
        traverse(graph,node, distance)
    
    return max(distance.values())

def traverse(graph, node, distance):
    if node in distance: return distance[node]

    max_dist = 0

    for neighbor in graph[node]:
        current = traverse(graph,neighbor,distance)
        max_dist = max(current,max_dist)
    distance[node] = 1 + max_dist 
    return distance[node]

graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': [],
  'q': ['r'],
  'r': ['s', 'u', 't'],
  's': ['t'],
  't': ['u'],
  'u': []
}

print(longest_path(graph))

'''
e: number of edges
n: number of nodes
Time Complexity: O(e)
Space COmplexity: O(n)
'''