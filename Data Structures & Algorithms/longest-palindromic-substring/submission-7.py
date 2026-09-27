class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=[[False]*len(s) for _ in range(len(s))]
 
        r,c=0,0

        #dont need to prefile wiht true, if its weird length like 2 then we can defualt to true via col-row<=2
        for row in range(len(dp)-1,-1,-1):
            for col in range(row+1,len(dp[0])):
                value=(s[row]==s[col] and (col-row<=2 or dp[row+1][col-1]))
                if value and col-row>c-r:
                    r,c=row,col
                dp[row][col]=value

        return s[r:c+1]
