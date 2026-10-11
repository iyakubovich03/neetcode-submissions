from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #tree each node has one parent (as long as this is hte case then its a valid tree)
        # set for idenitfying cycels 
        # map (parent to child)
        parentToChild=defaultdict(list)

        for a,b in edges:
            parentToChild[a].append(b)
            parentToChild[b].append(a)
    
        root=0   
        visited=set()

        def dfs(currentNode,previousNode):
            if currentNode in visited:
                return False
            visited.add(currentNode)
            for children in parentToChild[currentNode]:
                if children!=previousNode and not dfs(children,currentNode):
                    return False
            return True
       
        #need to find the root node 
        if not dfs(root,-1):
            return False
        return len(visited)==n
        # O(V+E) Space: O(V+E)
            


        