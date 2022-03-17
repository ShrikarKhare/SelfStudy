'''
Write a function, semesters_required, that takes in a number of courses (n) and a list of prerequisites as arguments. 
Courses have ids ranging from 0 through n - 1. 
A single prerequisite of (A, B) means that course A must be taken before course B. 
Return the minimum number of semesters required to complete all n courses. 
There is no limit on how many courses you can take in a single semester, 
as long the prerequisites of a course are satisfied before taking it.

Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester. 
You must take A in some semester before B.

You can assume that it is possible to eventually complete all courses.

test_00:
num_courses = 6
prereqs = [
  (1, 2),
  (2, 4),
  (3, 5),
  (0, 5),
]
semesters_required(num_courses, prereqs) # -> 3
test_01:
num_courses = 7
prereqs = [
  (4, 3),
  (3, 2),
  (2, 1),
  (1, 0),
  (5, 2),
  (5, 6),
]
semesters_required(num_courses, prereqs) # -> 5
'''

def semesters_required(num_courses, prereqs):
    graph = build_graph(num_courses, prereqs)
    distance = {}
    
    for node in graph: 
        if len(graph[node]) == 0:
            distance[node] = 1
    
    for node in graph:
        traverse(graph,node,distance)
    
    return max(distance.values())


def traverse(graph, node, distance):
    if node in distance: return distance[node]
    longest = 0
    for neighbor in graph[node]:
        current = traverse(graph,neighbor,distance)
        longest = max(longest, current)
    distance[node] = 1+ longest 
    return distance[node]

def build_graph(num_courses, prereqs):
    graph = {}
    
    for i in range(num_courses):
        graph[i] = []
    
    for prereq in prereqs:
        a,b  = prereq 
        graph[a].append(b)
    return graph 

num_courses = 7
prereqs = [
  (4, 3),
  (3, 2),
  (2, 1),
  (1, 0),
  (5, 2),
  (5, 6),
]
print(semesters_required(num_courses, prereqs)) # -> 5

'''
p : # prereqs
c : # courses
Time: O(p)
Space: O(c)
'''