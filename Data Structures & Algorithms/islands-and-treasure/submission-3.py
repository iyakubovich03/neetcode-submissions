import numpy as np
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        tracked=set()
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        que=deque()    
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==0:
                    que.append((row,col))  
        #now you have all the 0's , only need one que 

        #the major trick is we want to run bfs layer by layer(and if inf is updated then it is automaticly
        #the shortest one since it was updated first )
        while que:
            for i in range(len(que)):#GO THORUGH EACH LAYER AT ONCE
                row_v,col_v=que.popleft()
                #starts at 0 chekc direcitons
                for x,y in directions:
                    nx,ny=row_v+x,col_v+y
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==2147483647:
                        grid[nx][ny]=grid[row_v][col_v]+1
                        que.append((nx,ny))
                    #could have a problem where they explore all of htem 
    


        


        