class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #concept of pushing down one and then pusing down left
        res=[1 for j in range(len(nums))]
        prev=1
        for i in range(len(nums)):
            res[i]=prev
            prev*=nums[i]# mulitpleis at end so shifts left

        prev=1
        #now traverse leftwards then return 
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i]*prev
            prev*=nums[i]
        print(res)
        return res
