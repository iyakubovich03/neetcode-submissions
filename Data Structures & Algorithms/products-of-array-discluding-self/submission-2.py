class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[1 for i in range(len(nums))]
        prev=1
        j = 0
        for j in range(len(nums)):
            l[j]=prev
            prev*=nums[j]
        prev=1
        for t in range(len(nums)-1,-1,-1):
            l[t]*=prev
            prev*=nums[t]
        return l
