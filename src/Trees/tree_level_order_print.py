import collections
from collections import deque 
tree = [1,2,3,4,5,6] 

class Node:
    def __init__(self, val = None):
        self.left = None
        self.right = None
        self.val =val

# def levelOrderPrint(tree):
#     if not tree:
#        return
#     nodes = collections.deque([tree])
#     currentCount= 1
#     nextCount = 0
#     while len(nodes)!=0:
#         currentNode =nodes.popLeft()
#         currentCount-=1

#         print(currentCount.val)

#         if currentNode.left:
#             nodes.append(currentNode.left)
#             nextCount+=1
        
#         if currentNode.right:
#             nodes.append(currentNode.right)
#             nextCount+=1
#         if currentCount ==0:
#             currentCount =nextCount
#             print(currentCount)
#             nextCount= currentCount
#             print(nextCount)

def levelOrderPrint(tree):
    if not tree:
        return
    nodes=collections.deque([tree])
    currentCount, nextCount = 1, 0

    while len(nodes)!=0:
        currentNode=nodes.popleft()
        currentCount-=1
        print(currentNode.val)

        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount+=1

        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount+=1

        if currentCount==0:
            #finished printing current level
            currentCount =nextCount
            print(currentCount)
            nextCount= currentCount
            print(nextCount)

root = Node(1)
root.left = Node(2)
root.right = Node(3)

levelOrderPrint(root)


levelOrderPrint(tree)