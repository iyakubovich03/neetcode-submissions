class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        #heights array (integer) heights[i] is the height 
        #ocean view if every building to its right is smaller than it
        #return a list of indices sorted in increasing order 
        maxValue=-float('inf')
        result=[]
        for index in range(len(heights)-1,-1,-1):
            currentValue=heights[index]
            if currentValue>maxValue:
                result.append(index)
            maxValue=max(maxValue,currentValue)
        return result[::-1]

        