class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h=set()
        def checkIslands(row,col):
            if (row,col) in h or row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) or grid[row][col]=="0":
                return
            h.add((row,col))
            checkIslands(row+1,col)
            checkIslands(row-1,col)
            checkIslands(row,col+1)
            checkIslands(row,col-1)

        numIslands=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=="1" and (row,col) not in h:
                    numIslands+=1
                    checkIslands(row,col)
        return numIslands





        