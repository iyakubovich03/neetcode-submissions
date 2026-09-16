from collections import defaultdict,deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        pro={i : [] for i in range(numCourses)} #holds all of them 
        
        for a,b in prerequisites:
            pro[a].append(b)#maps class to prereq

        path=[]

        vis=set()#dont have to revisit nodes that have already been visited
        cycle=set()
        def dfs(course):

            if course in vis:
                return True
            if course in cycle:
                return False
             #already visited 
            cycle.add(course)#tracks the cycel if it loops

            for neigh in pro[course]:
                if not dfs(neigh):
                    return False
            #else it is true 
            vis.add(course)
            path.append(course)
            return True
            


                #should go to the end 
        for i in range(numCourses):#checks all paths 
            if not dfs(i):
                return []
        return path

                


        