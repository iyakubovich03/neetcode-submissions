class Node:
    def __init__(self,key,value,previous=None,nextV=None):
        self.key=key
        self.value=value
        self.previous=previous
        self.nextV=nextV
    
class LRUCache:

    def __init__(self, capacity: int):
        self.head=Node(0,0)
        self.tail=Node(0,0,self.head)
        self.head.nextV=self.tail
        self.cap=capacity
        self.nodeMap={}

    def add(self,node):
        lastNode=self.tail.previous

        lastNode.nextV=node
        self.tail.previous=node

        node.previous,node.nextV=lastNode,self.tail
    
    def deleteNode(self,key):
        previousNode,nextNode=self.nodeMap[key].previous,self.nodeMap[key].nextV
        previousNode.nextV=nextNode
        nextNode.previous=previousNode
        
    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        
        node=self.nodeMap[key]
        self.deleteNode(key)
        self.add(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key not in self.nodeMap and len(self.nodeMap)==self.cap:
            key1=(self.head.nextV).key
            self.deleteNode(key1)
            del self.nodeMap[key1]

        node=None
        if key in self.nodeMap:
            self.nodeMap[key].value=value
            node=self.nodeMap[key]
            self.deleteNode(key)

        if not node:
            node=Node(key,value)
            self.nodeMap[key]=node
        self.add(node)
        
        
        
