class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        def maxValue(start,end):
            step_1=0
            step_2=0
            for index in range(start,end):
                current=max(step_1,step_2+nums[index])
                step_1,step_2=current,step_1
            return step_1

        return max(maxValue(0,len(nums)-1),maxValue(1,len(nums)))

        