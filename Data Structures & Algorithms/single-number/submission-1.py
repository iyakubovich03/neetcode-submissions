class Solution:
    def singleNumber(self, nums: List[int]) -> int:
     

        """
        starting_value=0
        for number in nums:
            starting_value^=number
        return starting_value
        """
        nums.sort()
        index=0
        while index<len(nums):
            current_value=nums[index]
            if index+1<len(nums) and current_value==nums[index+1]:
                index=index+2
            else:
                return current_value
            
        