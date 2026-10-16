class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        check every element if not in the memo run dfs
        then enter and recruse till we cante xpand any more thatn grab the max value 
        update the path from tehre and update emom



        """
        memo={}
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        maxValue=-float('inf')
        def dfs(row,col):
            nonlocal maxValue
            if (row,col) in memo:
                return memo[(row,col)]
            path=0
            for dr,dc in direction:
                nr=row+dr
                nc=col+dc
                if 0<=nr<len(matrix) and 0<=nc<len(matrix[0]) and matrix[row][col]<matrix[nr][nc]:
                    path=max(path,dfs(nr,nc))
                
            memo[(row,col)]=path+1
            maxValue=max(maxValue,path+1)
            return path+1

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (row,col) not in memo:
                    dfs(row,col)

        return maxValue