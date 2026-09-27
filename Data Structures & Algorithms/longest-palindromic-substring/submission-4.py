class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=[[False]*len(s) for _ in range(len(s))]
        for row in range(len(dp)):
            for col in range(0,row+1):
                dp[row][col]=True
        r,c=0,0

        for row in range(len(dp)-1,-1,-1):
            for col in range(row+1,len(dp[0])):
                value=(s[row]==s[col] and dp[row+1][col-1])
                if value and col-row>c-r:
                    r,c=row,col
                dp[row][col]=value

        return s[r:c+1]
