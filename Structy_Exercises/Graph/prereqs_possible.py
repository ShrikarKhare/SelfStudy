'''
Write a function, prereqs_possible, that takes in a number of courses (n) and prerequisites as arguments. 
Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. 
The function should return a boolean indicating whether or not it is possible to complete all courses.
test_00:
numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
]
prereqs_possible(numCourses, prereqs) # -> True
test_01:
numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
  (3, 0),
]
prereqs_possible(numCourses, prereqs) # -> False
'''

def prereqs_possible(numCourses, prereqs):
    graph = build_graph(numCourses, prereqs)
    visiting = set()
    visited = set()

    for node in graph:
        if cycle(graph,node,visiting,visited):
            return False 
    return True 

def build_graph(numCourses, prereqs):
    graph = {}
    for i in range(numCourses):
        graph[i] = []
    for prereq in prereqs:
        a,b  = prereq 
        graph[a].append(b)
    return graph 

def cycle(graph,node,visiting,visited):
    if node in visiting: return True
    if node in visited: return False

    visiting.add(node)

    for neighbor in graph[node]:
        if cycle(graph,neighbor,visiting,visited):
            return True 
    visiting.remove(node)
    visited.add(node)
    return False

numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
]
print(prereqs_possible(numCourses, prereqs))