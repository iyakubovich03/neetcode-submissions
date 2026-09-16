class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited=set()
        for n in nums:
            visited.add(n)
        longest=0
        for v in visited:
            if v-1 not in visited:
                current=0
                while v in visited:
                    current+=1
                    v+=1
                longest=max(longest,current)
        return longest