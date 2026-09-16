class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        val=-float('inf')
        while l<r:
            less=heights[l] if heights[l]<heights[r] else heights[r]

            val=max(val,less*(r-l))
            if less==heights[l]:
                l+=1
            else:
                r-=1
        return val
            
        
