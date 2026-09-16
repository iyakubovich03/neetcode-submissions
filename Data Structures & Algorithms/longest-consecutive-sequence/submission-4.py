class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l=set(nums)
        y=0
        for i in nums:
            if i-1 not in l:
                z=1
                while i+z in l:
                    z+=1
                
                y=max(y,z)
        return y