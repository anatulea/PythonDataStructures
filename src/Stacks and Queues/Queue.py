# Implementation of Queue

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.insert(0, item) # insert item at index 0
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

q = Queue()

print(q.isEmpty()) #true

q.enqueue("first")
q.enqueue("second")
q.enqueue("third")
print(q.size()) # 3
print(q.dequeue()) # first
print(q.size()) # 2
print(q.dequeue()) # second 

