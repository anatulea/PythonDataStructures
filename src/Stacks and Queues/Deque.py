# Implement a Deque class

class Deque(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def addToRear(self, item):
        self.items.insert(0,item)
    
    def addToFront(self, item):
        self.items.append(item)
    
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

d = Deque()

d.addToFront("Hello")
d.addToRear("world")
print(d.removeFront() + " " + d.removeRear())