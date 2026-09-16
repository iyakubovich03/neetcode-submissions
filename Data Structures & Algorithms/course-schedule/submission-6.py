from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre=defaultdict(list)
        for a,b in prerequisites:
            pre[a].append(b)
        #have your mpa now run dfs
        color=[0]*numCourses
        def dfs(course):
            if color[course]==2:
                return True
            if color[course]==1:
                return False
            color[course]=1#visiting
        
            for neighbors in reversed(pre[course]):
                if dfs(neighbors)==False:
                    return False
            #else it was valid 
            color[course]=2#done visiting 
            return True
        
        for i in range(numCourses):
            if dfs(i)==False:
                return False
            
        return True


        



        