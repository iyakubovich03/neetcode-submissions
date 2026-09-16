import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        totalBanannas=sum(piles)
        l,r= 0,totalBanannas

        #now we iterate trying to minmize 
        #the concept is to iterate on with teh radius on binary search 
        
        def recursive(l,r,piles,k):
            if l==r:
                return r
            mid=l+(r-l)//2
            track=k
            i=0
            if mid==0:
                return 1
            while i<len(piles):
                currVal=piles[i]# this will reset need to stay here 
                while currVal>0 and track>0:
                    number=math.ceil(currVal/mid)# of times that fits into it
                    if number>track:
                        return recursive(mid+1,r,piles,k)
                    currVal-=(number*mid)
                    track-=number
                if currVal<=0:
                        i+=1  
                if track==0 and i<len(piles):
                    return recursive(mid+1,r,piles,k)
            #if it breaks out means valid 
            return recursive(l,mid,piles,k)
        return recursive(l,r,piles,h)

            


