class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        current=[]
        result=[]
        
        def backtrack(index):
            result.append(current.copy())
            if index==len(nums):
                return

            for ind in range(index,len(nums)):
                if ind>index and nums[ind]==nums[ind-1]:
                    continue
                #we take the element
                value=nums[ind]
                current.append(value)
                backtrack(ind+1)
                current.pop()

        backtrack(0)
        return result
                
        