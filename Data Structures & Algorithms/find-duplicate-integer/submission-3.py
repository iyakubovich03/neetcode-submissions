class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #floys algrothim (to find a cycle by using the vlaues as indexes)
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
            #meeting point 
        slow=0
        while nums[slow]!=nums[fast]:
            slow=nums[slow]
            fast=nums[fast]

        return nums[slow]





















        """
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
        """
            