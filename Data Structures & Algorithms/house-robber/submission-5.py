class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        one_step_back=0
        two_step_back=0

        for index in range(len(nums)):
            biggerValue=max(one_step_back,two_step_back+nums[index])
            one_step_back,two_step_back=biggerValue,one_step_back

        return one_step_back
        