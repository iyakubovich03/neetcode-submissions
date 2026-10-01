class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[-1]*(amount+1)
        dp[0]=0

        for index in range(1,len(dp)):
            value=float('inf')
            for coin in coins:
                if index>=coin and dp[index-coin]!=-1:
                    value=min(value,dp[index-coin]+1)
                    
            if value!=float('inf'):
                dp[index]=value

        return dp[-1]
