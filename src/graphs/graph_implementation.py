from enum import Enum
from collections import OrderedDict

class State(Enum):
    unviseted = 1
    viseted = 2
    visiting = 3

class Node:
    def __init__(self, num):
        self.num = num
        self.visit_state = State.unviseted
        self.adj = OrderedDict() # key = node, Value = weight
    
    def __str__(self):
        return str(self.num)

class Graph:

    def __init__(self):
        self.nodes = OrderedDict()

    def add_node(self, num):
        node = Node(num)
        self.nodes[num] = node
        return node

    def add_edge(self, source, dest, weight = 0):
        if source not in self.nodes:
            self.add_node(source)

        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[source].adj[self.nodes[dest]]= weight


g = Graph()
g.add_edge(0,1,5)
print(g.nodes)

g.add_edge(1,2,3)
print(g.nodes)