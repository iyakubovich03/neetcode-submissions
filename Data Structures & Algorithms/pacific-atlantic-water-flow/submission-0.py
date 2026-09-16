from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #hte idea is that we get two sets, one that can reach pacific, and one that can reach atalntic
        #get the intersection of that set
        pacific_set=set() #this will hold 
        atlantic_set=set()
        pacific_que=deque()
        atlantic_que=deque()

        for i in range(len(heights)):#over the rwos
            pacific_set.add((i,0))
            atlantic_set.add((i,len(heights[0])-1))
            pacific_que.append((i,0))
            atlantic_que.append((i,len(heights[0])-1))
        for j in range(len(heights[0])):#over the cols
            pacific_set.add((0,j))
            atlantic_set.add((len(heights)-1,j))
            pacific_que.append((0,j))
            atlantic_que.append((len(heights)-1,j))

        def bfs_trav(que,corr_set):
            #now the queues are fulled up 
            directions=[[-1,0],[1,0],[0,1],[0,-1]]
            while que:
                for i in range(len(que)):#layer by layer bfs
                    row,col=que.popleft()
                    for x,y in directions:
                        nx=row+x
                        ny=col+y
                        if 0<=nx<len(heights) and 0<=ny<len(heights[0]) and (nx,ny) not in corr_set and heights[nx][ny]>=heights[row][col]:
                            corr_set.add((nx,ny))
                            que.append((nx,ny))
        bfs_trav(pacific_que,pacific_set)
        bfs_trav(atlantic_que,atlantic_set)
        #now we want intersection of both 
        total_set=[]
        for a,b in pacific_set:
            if (a,b) in atlantic_set:
                total_set.append([a,b])
        return total_set
