class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return amount
        if min(coins)>amount:
            return -1

        dp=[-1]*(amount+1)

        for coin in coins:
            if coin<len(dp):
                dp[coin]=1

        #now j iterate forward n 
        for index in range(len(dp)):
            currentValue=dp[index]

            if currentValue!=-1:
                continue

            value=float('inf')
            for coin in coins:
                previousValue=dp[index-coin] if index>=coin else -1
                if previousValue==-1:
                    continue
                value=min(value,previousValue+1)
            if value!=float('inf'):
                dp[index]=value

        return dp[-1]
