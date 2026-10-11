from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components=0
        adjList=defaultdict(list)
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visited=set()
        def dfs(currentNode,previousNode):
            visited.add(currentNode)
            for children in adjList[currentNode]:
                if children not in visited:
                    dfs(children,currentNode)

        for node in range(n):
            if node not in visited:
                components+=1
                dfs(node,-1)
        return components
        #(Node+Edge) O(Node+edge)