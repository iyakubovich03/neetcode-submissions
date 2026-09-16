class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #basically we are checkign for a cycle 
        #lets run dfs on each node and if we get back to ti somehow
        #create weird ajdacnecy list
        adj={i : [] for i in range(n)}
        #now populate it
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)#not directed can go from either point but once explored you cannot go back 
            #adj[b].append(a)#not directed but once you explore that path you cannot go back
        #key def that cycle is created when you can get to a previous vertex via a DIFFERENT EDGE
        #it would still be in visited state 
        count=0
        #color=[0]*n
        visited=set()#so we dont go back on the same edge

        #or we can just count vertices not track vertices n not track if has been visited already or not 
        #as long as you dont go back to the previous node if
        def dfs(course,prev):
            nonlocal count
            #just chekc if no cycles n connected 
            if course in visited:
                return False
            visited.add(course)#adds to visited
            count+=1
            for neigh in adj[course]:
                if neigh!= prev:#two cases
                    if neigh in visited:
                        return False
                    else:
                        dfs(neigh,course)
        
            return True
        
        val=dfs(0,-1)
        if count<n:
            return False
        return val

    
    

        