class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None

# create the nodes
a = Node(1)
b = Node(2)
c = Node(3)

# connect the nodes
a.nextnode = b
b.nextnode = c
print(nextnode.value)