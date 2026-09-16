class Solution:
    def trap(self, height: List[int]) -> int:
        lmax,rmax=0,0
        l,r=0,len(height)-1
        totalWater=0
        while l<=r:
            if height[l]<height[r]:#limited by this side
                lmax=max(lmax,height[l])
                totalWater+=lmax-height[l]
                l+=1
            else:
                rmax=max(rmax,height[r])
                totalWater+=rmax-height[r]
                r-=1
        return totalWater

        