class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = {}
        y =[]
        for i in range(len(nums)):
            if (target-nums[i] in l):
                return [l.get(target-nums[i]),i]
            l[nums[i]]=i
        
        