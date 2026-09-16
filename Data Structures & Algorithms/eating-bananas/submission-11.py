import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        totalBanannas=max(piles)
        l,r= 1,totalBanannas # the lower bound 

        #now we iterate trying to minmize 
        #the concept is to iterate on with teh radius on binary search 
        
        def recursive(l,r,piles,k):
            if l==r:
                return r
            mid=l+(r-l)//2
            totalHours=0
            totalHours=sum(math.ceil(r/mid) for r in piles)
            if totalHours>k:# not valid recurse right 
                return recursive(mid+1,r,piles,k)
            return recursive(l,mid,piles,k)
            
        return recursive(l,r,piles,h)

            


