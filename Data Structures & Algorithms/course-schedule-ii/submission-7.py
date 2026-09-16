from collections import defaultdict,deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        pro={i : [] for i in range(numCourses)} #holds all of them 
        
        for a,b in prerequisites:
            pro[a].append(b)#maps class to prereq

        path=[]
        #0 means unvisited chill
        #1 means visitng cycle
        #2 means fully explored
        color=[0]*numCourses
        def dfs(course):

            if color[course]==2: #this order matters
                return True
            if color[course]==1:#means visiting already so encountered cyle
                return False
            color[course]=1 #set equal to 1 one means it is being visited
            for neigh in pro[course]:
                if not dfs(neigh):
                    return False
            #else it is true 
            color[course]=2#done explroing 
            path.append(course)
            return True
            


                #should go to the end 
        for i in range(numCourses):#checks all paths 
            if not dfs(i):
                return []
        return path

                


        