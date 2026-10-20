class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max=nums[0]
        current_sum=nums[0]

        for index in range(1,len(nums)):
            current_value=nums[index]
            current_sum=max(current_sum+current_value,current_value)
            global_max=max(global_max,current_sum)
            
        return global_max

        