"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #traverse over the adjacent list keep track of explored 
        #each vlaue in the neihgbor should be anode itself
        if not node:
            return None
        explored=set()
        track={} #connects nodes to neighbros 
        current_node=node #current node 
        temp=[] # the que
        temp.append(current_node)
        while temp:
            curr_val=temp.pop(0)
            
            #current Node, maybe we can set neighbors to the values that we will assing in teh future 
            if curr_val not in track:
                track[curr_val]=Node(curr_val.val,[])
            explored.add(curr_val)
            print(curr_val.neighbors)
            for i in curr_val.neighbors:
                
                if i not in track:
                    track[i]=Node(i.val,[])
                track[curr_val].neighbors.append(track[i])#adds as refrence 
                #need to repopulate the que 
                if i not in explored and i not in temp:#if not explored adds to temp
                    temp.append(i)
        
        return track[node]

                
           



