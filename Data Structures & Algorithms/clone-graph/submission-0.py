"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #what is the break condition 
        t=set()
        l={}
        if not node:
            return
        def pot(root):
            nonlocal t
            if root.val in t:
                return l[root]# returning the same val need cloned
            new=Node(root.val)
            l[root]=new
            t.add(root.val)
            if root.neighbors:
                for i in root.neighbors:
                    new.neighbors.append(pot(i))
            else:
                new.neighbors=[]
            
            return new

        return pot(node)

        # iterate forward as well as create the node assign it the same engihrbors #they are nodes
