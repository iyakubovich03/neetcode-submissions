class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0 
        r = len(heights)-1
        max=0
        while l<r:
            lower = heights[l] if heights[l]<heights[r] else heights[r]
            max = lower*(r-l) if (lower*(r-l)>max) else max
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
            
            
        return max   