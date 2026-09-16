from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximumValues=deque()
        result=[]

        for index,value in enumerate(nums):
            #pop once the size
            if maximumValues and index-k==maximumValues[0]:
                maximumValues.popleft()
            while maximumValues and nums[maximumValues[-1]]<value:
                maximumValues.pop()
            maximumValues.append(index)
            if (index-k+1)>=0:
                result.append(nums[maximumValues[0]])
        return result
      