'''
Write a function, has_cycle, that takes in an object representing the adjacency list of a directed graph. 
The function should return a boolean indicating whether or not the graph contains a cycle.

test_00:
has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
}) # -> True
test_01:
has_cycle({
  "a": ["b", "c"],
  "b": ["c"],
  "c": ["d"],
  "d": [],
}) # -> False
'''

def has_cycle(graph):
    visiting = set()
    visited = set()

    for node in graph:
        if cycle(graph,node,visiting,visited):
            return True
    return False 

def cycle(graph, node, visiting,visited):
    if node in visiting: return True
    if node in visited: return False 
    visiting.add(node)

    for neighbor in graph[node]:
        if cycle(graph,neighbor,visiting,visited):
            return True 
    visiting.remove(node)
    visited.add(node)
    return False 

graph = {
  "a": ["b", "c"],
  "b": ["c"],
  "c": ["d"],
  "d": [],
} # -> False
graph = {
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
}
print(has_cycle(graph))