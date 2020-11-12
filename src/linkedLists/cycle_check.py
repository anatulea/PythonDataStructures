class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None



def cycle_check(node):
#     Use fast and slow pointer
    fast, slow = node, node
    while fast and fast.nextnode:
        fast = fast.nextnode
        if fast == slow:
            return True
        fast = fast.nextnode
        slow = slow.nextnode
    return False

