class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        minSell=float('inf')
        for price in prices:
            minSell=min(minSell,price)
            maxProfit=max(maxProfit,price-minSell) 
        return maxProfit
        