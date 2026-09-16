class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #the bigger number get
        stack=[]
        #idea if we hit a smaller value ,take the max of it and continue looping making it smaler, 
        #then at the end do some iteratoin and 
        maxRectangle=0
        for index,height in enumerate(heights):
            startIndex=index
            while stack and stack[-1][0]>height:
                prevHeight,prevIndex=stack.pop()
                maxRectangle=max(maxRectangle,prevHeight*(index-prevIndex))
                startIndex=prevIndex
            stack.append((height,startIndex)) #(value,index)
        for v,start in stack:
            maxRectangle=max(maxRectangle,(len(heights)-start)*v)
        return maxRectangle

        #at the end now iterate 
        


        