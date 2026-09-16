from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre=defaultdict(list)
        for a,b in prerequisites:
            pre[a].append(b)
        #have your mpa now run dfs
        visited=set()
        def dfs(course):
            if course in visited:#explore each 
                return False
            if pre[course]==[]:
                return True
            visited.add(course)
        
            for neighbors in reversed(pre[course]):
                if dfs(neighbors)==False:
                    return False
            #else it was valid 
            visited.remove(course)
            pre[course]=[]
            return True
        
        for i in range(numCourses):
            if dfs(i)==False:
                return False
            
        return True


        



        