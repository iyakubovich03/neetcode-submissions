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
            #both ways 

        root=None
        for key,value in parentToChild.items():
            if len(value)==1:
                root=key
                break
            
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

        print(f"number of nodes seen {len(visited)}")
        return len(visited)==n
            


        