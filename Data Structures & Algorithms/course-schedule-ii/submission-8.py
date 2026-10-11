class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseToPrereq=[[] for _ in range(numCourses)]

        for course,pre in prerequisites:
            courseToPrereq[course].append(pre)

        color=[0]*numCourses #0 not explored #1  currently exploring #2 fully explored 
        result=[]

        def dfs(course):
            if color[course]==2:
                return True
            elif color[course]==1:
                return False

            color[course]=1

            for pre in courseToPrereq[course]:
                if not dfs(pre):
                    return False
            result.append(course)
            color[course]=2
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return result
        