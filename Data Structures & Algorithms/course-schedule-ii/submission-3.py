from collections import defaultdict,deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #we check for cycle 
        #if no cycle then return an ordering of bfs , make sure all courses are added 
        """
        pre={i : [] for i in range(numCourses)} #holds all of them 
        for a,b in prerequisites:
            pre[b].append(a)#maps prerequs to classes 
        print(pre)
        
        #now we have our list 
        #we can track the list 
        #add regardless
        valid_path=[]
        
        def bfs(course):
            visited=set()
            que=deque()
            que.append(course)
            while que:
                curr=que.popleft()
                if curr in visited:#means the bfs ran into a loop here
                    return False #
                valid_path.append(curr) #adds to the path
                visited.add(curr)#adds to visited
                for neighbors in pre[curr]:#adds neihgbors to end
                    que.append(neighbors)
            return True
        """

        pro={i : [] for i in range(numCourses)} #holds all of them 
        for a,b in prerequisites:
            pro[a].append(b)#maps class to prereq

        vis=set()
        path=[]

        def dfs(course):
            if course in vis:
                return False
            if pro[course]==[]:
                if course not in path:
                    path.append(course)
                return True
            vis.add(course)
            for neigh in pro[course]:
                if not dfs(neigh):
                    return False
                #otherwise true 
            vis.remove(course)
            pro[course]=[]
            #now we add to the path 
            path.append(course)
            return True


                #should go to the end 
        for i in range(numCourses):#checks all paths 
            if i not in path:
                if not dfs(i):
                    return []
        return path

                


        