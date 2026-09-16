from collections import deque
class Solution:
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #start off at 2nd value 
        #from here you will run dfs or bfs but you increment to a global variable 
        tracked=set()
        count_of_fruits=0
        minutes=0
        directions=[[-1,0],[1,0],[0,1],[0,-1]]
        que=deque()
        #track number of fresh fruits
        #get intial rotten banaa postion
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==2:
                    que.append((row,col))
                elif grid[row][col]==1:
                    count_of_fruits+=1
        if not count_of_fruits: # eraly return 
            return 0
        #this is O(m*n)
        #if neighbor 1 add to que n incrment 
        while que:
            for i in range(len(que)):# layer by layer but only add once
                row,col=que.popleft()
                tracked.add((row,col))
                for x,y in directions:
                    nx,ny=row+x,col+y
                    #if valid bounds
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and (nx,ny) not in tracked and grid[nx][ny]==1:
                     
                        count_of_fruits-=1#tracking number that turned rotten 
                        tracked.add((nx,ny))
                        que.append((nx,ny))
            if que:#if que then bannas turned rotten else didnt 
                minutes+=1

        if count_of_fruits:
            return -1
        else:
            return minutes
        
        


        