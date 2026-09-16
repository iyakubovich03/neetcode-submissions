class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousValues={} #O(N)
        for index,value in enumerate(nums): #O(N)
            if target-value in previousValues:
                return [previousValues[target-value],index]
            previousValues[value]=index
        return [-1,-1]
        