graph1 = {
    'A': set(['B', 'C']),
    'B': set(['A','D','E']),
    'C': set(['A','F']),
    'D': set(['B']),
    'E': set(['B','F']),
    'F': set(['C','E'])
}

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)

            stack.extend(graph[vertex]-visited)
    return visited

# print(dfs(graph1, 'A'))

def dfs2(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for nxt in graph[start] - visited:
        dfs2(graph, nxt, visited) # recursion
    return visited

# print(dfs2(graph1, 'A'))


'''
Paths
We are able to tweak both of the previous implementations to return all possible paths between a start and goal vertex. The implementation below uses the stack data-structure again to iteratively solve the problem, yielding each possible path when we locate the goal. Using a generator allows the user to only compute the desired amount of alternative paths.

1.Start at a vertex.
2.Pick any unvisited vertex adjacent to the current vertex, and check to see if this is the goal.
3.If not, recursively apply the depth-first search to that vertex, ignoring any vertices that have already been visited.
4.Repeat until all adjacent vertices have been visited.

<<<
Recursive DFS for large graphs can exceed the maximum recursion calls
A better way would be to use stacks 

visitedNodes = set()
def depthFirst(node, soughtValue, visitedNodes):
   if node.value == soughtValue:
      return True
 
   visitedNodes.add(node)
   for adjNode in node.adjacentNodes:
      if adjNode not in visitedNodes:
         if depthFirst(adjNode, soughtValue, visitedNodes):
            return True
 
   return False
>>>

<<<
-----  USING STACKS   ---------

def depthFirst(startingNode, soughtValue):
   visitedNodes = set()
   stack = [startingNode]
 
   while len(stack) > 0:
      node = stack.pop()
      if node in visitedNodes:
         continue
 
      visitedNodes.add(node)
      if node.value == soughtValue:
         return True
 
      for n in node.adjacentNodes:
         if n not in visitedNodes:
            stack.append(n)
   return False
<<<
'''

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                stack.append((nxt, path + [nxt]))

print(list(dfs_paths(graph1, 'A', 'F')))