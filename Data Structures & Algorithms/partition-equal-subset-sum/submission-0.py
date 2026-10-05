class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        half=total/2

        if half!=int(half):
            return False

        def recurse(index,value):
            if value==half:
                return True
                
            if index==len(nums):
                return False
            
            found=False
            for ind in range(index,len(nums)):
                currentValue=nums[ind]
                found=found or recurse(ind+1,value+currentValue)

            return found
        
        return recurse(0,0)

            
        