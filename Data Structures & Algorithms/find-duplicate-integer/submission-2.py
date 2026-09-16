class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # value-1 check if repeated if not continue, and swap, only move pointer when 
        #satisfied 
        pointer=0

        while pointer<len(nums):
            currentValue=nums[pointer]
            if pointer==currentValue-1:
                pointer+=1
                continue
            if nums[currentValue-1]==currentValue:
                return currentValue
            nums[currentValue-1],nums[pointer]=currentValue,nums[currentValue-1]

        return -1
            