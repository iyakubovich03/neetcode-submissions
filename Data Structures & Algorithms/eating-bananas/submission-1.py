class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        x=max(piles) # bascilly binary over small to max (checks if values will add up to h and if it is or less than it will continue to go less than  to try to get least number n then set equal to val )
        y=1
        ans=y
        while y<=x:
            mid=(x+y)//2
            z=0
            for i in piles:
                z+= math.ceil((i) /mid) #needs to go jp
            
            if z>h:
        
                y=mid+1
            if z<=h:
                ans=mid
                x=mid-1
        return ans



    

