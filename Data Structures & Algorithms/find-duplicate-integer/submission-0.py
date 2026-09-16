class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l={}
        for i,v in enumerate(nums):
            if v in l:
                return v
            l[v]=i

