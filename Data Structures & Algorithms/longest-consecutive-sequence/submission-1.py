class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x=0
        for i in nums:
            p=1
            if i-1 not in nums:
                while i+1 in nums:
                    p+=1
                    i =i+1
            if p>x:
                x=p
        return x
        