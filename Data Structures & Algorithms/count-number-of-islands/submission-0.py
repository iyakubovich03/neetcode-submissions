class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h=set()
        counter=0
        def pot(tup):
            row,col=tup
            nonlocal h
            if (row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) or (row,col) in h or grid[row][col]!="1"):
                return False #base case
            h.add((row,col))
            pot((row+1,col))
            pot((row-1,col))
            pot((row,col+1))
            pot((row,col-1))

            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col]=="1" and (row,col) not in h):
                    counter+=1
                    pot((row,col))
        return counter
        


        