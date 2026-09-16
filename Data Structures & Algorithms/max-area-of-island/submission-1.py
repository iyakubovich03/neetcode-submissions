class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count=0
        glob=0
        h=set()
        def checker(typ):
            nonlocal count
            nonlocal glob
            nonlocal grid
            row,col=typ
            if (row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) or (row,col) in h or grid[row][col]!=1):
                return False
            h.add((row,col))
            count+=1
            checker((row+1,col))
            checker((row-1,col))
            checker((row,col+1))
            checker((row,col-1))
           
            
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                count=0
                if (row,col) not in h and grid[row][col]==1:
                    checker((row,col))
                    glob=max(glob,count)
        return glob

