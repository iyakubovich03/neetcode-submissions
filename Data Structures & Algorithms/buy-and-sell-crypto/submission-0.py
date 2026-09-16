class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        y=0
        for i in range(0,len(prices)-1,1):
            x=0
            for l in range(i+1,len(prices),1):
                x=prices[l]-prices[i]
                if x>y:
                    y=x
        return y

        