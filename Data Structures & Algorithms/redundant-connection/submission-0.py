from collections import deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
       
        def dfs(start,prev):#the point of this dfs is to show if a cycle occurs
            if start in visited:
                return True
            visited.add(start)
            for neigh in adjList[start]:
                if neigh==prev:
                    continue
                if neigh in visited:
                    return True
                if dfs(neigh,start):
                    return True
            #if no cycle
            return False

        adjList={i : [] for i in range(1,len(edges)+1)}
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)#since undirected add to both sides
            #now need to track visited set
            visited=set()
            if dfs(a,-1):
                return [a,b]
        #might b an edge case
            

            #ecah edge add to teh adjList