'''
Given the Stack class below, implement a Queue class using two stacks
'''
class Queue2Stacks(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def enqueue(self, ele):
        self.in_stack.append(ele)
    
    def dequeue(self):
        
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)
    
for i in range(5):
    print (q.dequeue())