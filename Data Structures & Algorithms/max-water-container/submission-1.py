class Solution:
    def maxArea(self, heights: List[int]) -> int:
        val=-1000
        l=0
        r=len(heights)-1
        while l<r:
            if (heights[l]<heights[r]):
                val=max(val,heights[l]*(r-l))
                l+=1
            elif (heights[l]>heights[r]):
                val=max(val,heights[r]*(r-l))
                r-=1
            else:
                val=max(val,heights[r]*(r-l))
                r-=1
        return val
