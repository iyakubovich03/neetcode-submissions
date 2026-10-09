from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        deq=deque()
        freshFruit=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==2:
                    deq.append((row,col))
                elif grid[row][col]==1:
                    freshFruit+=1

        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        minutes=0
        while deq:
            made_rotten=0
            for _ in range(len(deq)):
                current_row,current_col=deq.popleft()
                for dr,dc in directions:
                    new_row=current_row+dr
                    new_col=current_col+dc 
                    if 0<=new_row<len(grid) and 0<=new_col<len(grid[0]) and grid[new_row][new_col]==1:
                        grid[new_row][new_col]=2
                        made_rotten+=1
                        deq.append((new_row,new_col))
            if made_rotten==0:
                break 
            freshFruit-=made_rotten
            minutes+=1

        return minutes if freshFruit==0 else -1
                    


        