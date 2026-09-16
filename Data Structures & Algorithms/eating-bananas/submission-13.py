class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,sum(piles)
        while l<r:
            mid=l+(r-l)//2
            if self.checkValid(mid,piles,h):
                r=mid
            else:
                l=mid+1
        return r


    def checkValid(self,rate,piles,h):
        numberOfHours=0
        for pile in piles:
            numberOfHours+=math.ceil(pile/rate)
        #valid if less or euqal hours
        return numberOfHours<=h
        