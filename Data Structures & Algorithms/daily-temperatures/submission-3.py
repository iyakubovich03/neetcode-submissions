class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        smallerValues=[] #the index
        result=[0]*len(temperatures)
        for index,value in enumerate(temperatures): #O(N) #worst case O(2N)
            while smallerValues and value>temperatures[smallerValues[-1]]:
                prevIndex=smallerValues.pop()
                prevValue=temperatures[prevIndex],
                result[prevIndex]=index-prevIndex
            #append the value 
            smallerValues.append(index)
        return result