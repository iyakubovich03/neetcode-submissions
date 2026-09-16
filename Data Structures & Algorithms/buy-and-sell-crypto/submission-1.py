class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        l=0
        r=1
        track=0
        val=0

        #simple slidewing widnow
        while r<len(prices): #so it doesnt gov over
            if(prices[r]>prices[l]):
                val=max(val,prices[r]-prices[l])
            else:
                l=r
            r+=1
        return val

        