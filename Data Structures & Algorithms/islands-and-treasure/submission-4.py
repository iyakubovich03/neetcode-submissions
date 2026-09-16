
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        que=deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if not grid[row][col]:
                    que.append([row,col])
        #now we have all teh start off points
        four_directions=[[-1,0],[1,0],[0,-1],[0,1]]
        
        while que:
            
            row,col=que.popleft()#O(1)
            #now check fourdirections
            for a,b in four_directions:
                y=row+a
                x=col+b
                if 0<=y<len(grid) and 0<=x<len(grid[0]) and grid[y][x]==2147483647:#if valud
                  
                    grid[y][x]=grid[row][col]+1
                    que.append([y,x])
        #multisource bfs instead of recursing from every infinty which could has alot of repeption 
        #can j go from soruce 


                #


        #trasnfer all the points to teh que 
    
        


        