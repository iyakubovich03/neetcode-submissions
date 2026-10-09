from collections import deque
class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        deq=deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==0:
                    deq.append((row,col,0))
        
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while deq:
            current_row,current_col,current_distance=deq.popleft()
            for dr,dc in directions:
                new_row=current_row+dr
                new_col=current_col+dc
                if 0<=new_row<len(grid) and 0<=new_col<len(grid[0]) and grid[new_row][new_col]==2147483647:
                    grid[new_row][new_col]=current_distance+1
                    deq.append((new_row,new_col,current_distance+1))
        


        