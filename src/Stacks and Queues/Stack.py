# Implementation of a stack
class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == [] # returns True if list is empty, False if there are items in the list
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return (self.items[len(self.items)-1]) # returns the last item added
    
    def size(self):
        return len(self.items)

s = Stack()
print(s.isEmpty()) #True
s.push('one')
s.push('two')
s.push('three')
print(s.peek()) # three
s.pop()
print(s.peek())# two
print(s.isEmpty()) # False
