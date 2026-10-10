class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPre=[[] for _ in range(numCourses)]
        for a,b in prerequisites:
            courseToPre[a].append(b) #course to preReq
        topSort=[0]*numCourses

        def dfs(current):
            if topSort[current]==2:
                return True
            elif topSort[current]==1:
                return False
            
            topSort[current]=1
            #explore neighbros
            value=True
            for neighbor in courseToPre[current]:
                value= value and dfs(neighbor)
            topSort[current]=2
            return value 
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

                
        
        