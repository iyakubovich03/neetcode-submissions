class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        step_1=0
        step_2=0
        maxValue=0
        for index in range(len(nums)-1):
            current=max(step_1,step_2+nums[index])
            step_1,step_2=current,step_1
        maxValue=max(maxValue,step_1)
        step_1=0
        step_2=0

        for index in range(len(nums)-1,0,-1):
            current=max(step_1,step_2+nums[index])
            step_1,step_2=current,step_1

        return max(maxValue,step_1)
        