'''
Write a function that takes a head node and an integer value n and then returns the nth to last node in the linked list. For example, given:
'''

class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

def nth_to_last_node(n, head):
    slow, fast = head, head
    while n > 0 and fast:
        fast=fast.nextnode
        n-=1
    if not fast:
        return head
    while fast:
        fast=fast.nextnode
        slow=slow.nextnode
    return slow

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(2, a)
print(target_node.value)