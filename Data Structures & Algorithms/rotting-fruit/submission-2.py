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
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==2:
                    que.append((row,col))
                elif grid[row][col]==1:
                    count_of_fruits+=1
        #this is O(m*n)
        #if neighbor 1 add to que n incrment 
        count_of_rotten=0
        print(que)
        while que:
            for i in range(len(que)):# layer by layer but only add once
                row,col=que.popleft()
                tracked.add((row,col))
                for x,y in directions:
                    nx,ny=row+x,col+y
                    #now check condtions n add ones
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and (nx,ny) not in tracked and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        count_of_rotten+=1
                        tracked.add((nx,ny))
                        que.append((nx,ny))
            if que:
                minutes+=1

        if count_of_rotten<count_of_fruits:
            return -1
        elif count_of_rotten==count_of_fruits:
            return minutes
        
        


        