class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1
        for row in range(m):
            for col in range(n):
                if row==0 and col==0:
                    continue
                    
                left_value=dp[row][col-1] if col>0 else 0
                up_value=dp[row-1][col] if row>0 else 0
                dp[row][col]=left_value+up_value
        print(dp)
        return dp[-1][-1]        