class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       l=[]
       for i in nums:
            if i in l:
                return i
            l.append(i)

