class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #connected components
        adjL={i:[] for i in range(n)}
        for a,b in edges:
            adjL[a].append(b)
            adjL[b].append(a)

        visited=set()
        #if connected then it will be visited 
        #we terminate once all points are visited 
        
        def dfs(point,prev):
            if point in visited:
                return 
            visited.add(point)#track viisted 
            #now recurse on it engihbros
            for neigh in adjL[point]:
                if neigh!=prev:
                    dfs(neigh,point)    
            return     
            
        #it just needs to run dfs accorss all teh nodes 
            #this shohld run 
        print(adjL)
        
        count=0
        for i in range(n):
            print(f"this is i : {i}")

            if i not in visited:
                dfs(i,-1)
                print(f"this is the visited {visited}")
                count+=1
        return count