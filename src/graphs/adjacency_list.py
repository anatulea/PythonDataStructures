class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    # add connections from this vertex to another
    def addNeighbor( self, nbr, weight = 0): 
        self.connectedTo[nbr]= weight

    # returns all the vertices in the adjacency list 
    def getConnections(self):
        return self.connectedTo.keys()
    
    # returns the id or vertix name
    def getId(self):
        return self.id
    
    # returns the weight from this vertex to the vertex passed as a parameter
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
    
    def __str__(self):
        return str(self.id)+ ' connected to: ' + str([x.id for x in self.connectedTo])

# create an empty graph 
class Graph: 
    def __init__(self):
        self.vertList = {} # ADJACENCY LIST FORM - Its a dictionary
        self.numVertices = 0
    
    # adds an instance of Vertex to the graph
    def addVertex(self, key):
        self.numVertices +=1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    # finds the vertex in the graph named n 
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    # adds a new, directed edge to the graph that conects two vertices
    def addEdge(self, f,t,cost =0): # f - from vertex,  t - to vertex,  cost - weight
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        
        self.vertList[f].addNeighbor(self.vertList[t], cost)
    
    # returns the list of all the vertics in the graph
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())
    
    def __contains__(self, n):
        return n in self.vertList

g = Graph()
for i in range(6):
    g.addVertex(i)

print(g.vertList)
g.addEdge(0,1,2)

for vertex in g:
    print(vertex)
    print(vertex.getConnections())