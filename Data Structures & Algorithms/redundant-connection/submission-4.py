from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # O(N) * O(V+E) (popping from the end or deleting that edge) and checking if its cycle or not
        #
        parent=[i for i in range(len(edges)+1)]
        size=[1]*(len(edges)+1)
        
        def find(node):
            if parent[node]==node:
                return node #parent
            
            parent[node]=find(parent[node]) #backfill O(1) 

            return parent[node]

        def union(node_1,node_2):

            parent_1=find(node_1)
            parent_2=find(node_2)

            if parent_1==parent_2:
                return False #cycle

            if size[parent_1]<size[parent_2]:
                parent_1,parent_2=parent_2,parent_1

            parent[parent_2]=parent_1
            size[parent_1]+=size[parent_2]
            return True
        # O(1) on average worse case Log(N)
        for node1,node2 in edges:
            if not union(node1,node2):
                return [node1,node2]

            

            


        