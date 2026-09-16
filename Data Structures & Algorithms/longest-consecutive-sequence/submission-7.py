class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()#puts in sorted order
        val=0
        track=1
        for i in range(len(nums)):
            if (i>0 and nums[i]==nums[i-1]):
                continue# equivlance case 
            if (i>0 and nums[i]==nums[i-1]+1):
                track+=1
            elif (i>0 and nums[i]!=nums[i]-1):
                track=1
            val=max(val,track)
        return val
            