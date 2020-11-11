'''
Breath-First -SEarch
Returns the shortest path
'''
graph1 = {
    'A': set(['B', 'C']),
    'B': set(['A','D','E']),
    'C': set(['A','F']),
    'D': set(['B']),
    'E': set(['B','F']),
    'F': set(['C','E'])
}

def BFS(graph, start):
    visited = set()
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex]- visited)
    return visited
print(BFS(graph1, 'A'))


# return all possible paths between two vertices, 
# the first of which being one of the shortest such path.

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

print(list(bfs_paths(graph1, 'A', 'F')))


'''
Knowing that the shortest path will be returned first from the BFS path generator method we can create a useful method which simply returns the shortest path found or ‘None’ if no path exists. As we are using a generator this in theory should provide similar performance results as just breaking out and returning the first matching path in the BFS implementation.
'''
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

print(shortest_path(graph1, 'A', 'F'))

"""
BFS using deque
"""
from collections import deque
 
def breadthFirst(startingNode, soughtValue):
   visitedNodes = set()
   queue = deque([startingNode])
 
   while len(queue) > 0:
      node = queue.pop()
      if node in visitedNodes:
         continue
 
      visitedNodes.add(node)
      if node.value == soughtValue:
         return True
 
      for n in node.adjacentNodes:
         if n not in visitedNodes:
            queue.appendleft(n)
   return False