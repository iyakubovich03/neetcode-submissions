class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l=0
        r=len(height)-1
        total=0
        maxL=height[l]
        maxR=height[r]
        while (l<r):
            if maxR<maxL:
                r-=1
                maxR=max(height[r],maxR) 
                total+=(maxR-height[r])
            else:
                l+=1
                maxL=max(height[l], maxL)
                total+=(maxL-height[l])
        return total         