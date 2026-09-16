class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        h=set()
        maV=-float('inf')
        track=1
        nums.sort()
        for i in range(len(nums)):
            if nums[i] in h: 
                continue
            if i>0 and nums[i]==nums[i-1]+1:
                track+=1
            else:
                track=1
            h.add(nums[i])
            maV=max(maV,track)
        return maV
