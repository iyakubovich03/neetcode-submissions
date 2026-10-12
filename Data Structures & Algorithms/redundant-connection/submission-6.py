from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # T: O(E) S: O(N) 

        #create the adj list
        #find the edge where teh cycel 'ends'
        #also we will track teh parent ndoe we came from so we can backtrack 

        adjList=defaultdict(list)
        visited=set()
        parent={}

        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        def dfs(current,prev):
            visited.add(current)
            parent[current]=prev
            
            
            for neighbor in adjList[current]:
                if neighbor==prev:
                    continue
                if neighbor in visited:
                    return current,neighbor
                start,end=dfs(neighbor,current)
                if start is not None:
                    return start,end

            return None,None

        start,end=dfs(1,-1)
        print(start,end)
        #cycel loop
        cycle={(start,end)}
        while start!=end:
            startParent=parent[start]
            cycle.add((startParent,start))
            start=startParent
        print(cycle)
        #from here we need 

        for index in range(len(edges)-1,-1,-1):
            nodeA,nodeB=edges[index]
            if (nodeA,nodeB) in cycle or (nodeB,nodeA) in cycle:
                return edges[index]

        

            #we traverse 

                


        """
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
        """
            

            


        