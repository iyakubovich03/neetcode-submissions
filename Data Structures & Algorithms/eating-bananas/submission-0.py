class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        x=max(piles)
        y=1
        ans=y
        while y<=x:
            mid=(x+y)//2
            z=0
            for i in piles:
                z+= math.ceil(float(i) /mid)
            
            if z>h:
        
                y=mid+1
            if z<=h:
                ans=mid
                x=mid-1
        return ans



    

