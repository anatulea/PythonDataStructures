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
Paths¶
We are able to tweak both of the previous implementations to return all possible paths between a start and goal vertex. The implementation below uses the stack data-structure again to iteratively solve the problem, yielding each possible path when we locate the goal. Using a generator allows the user to only compute the desired amount of alternative paths.
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