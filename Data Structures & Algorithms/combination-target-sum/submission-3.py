class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        current=[]
    
        def backtrack(index,currentSum):
            if currentSum==target: #equal good
                result.append(current.copy()) #O(N)
                return

            if currentSum>target or index==len(nums): # over stop
                return

            for ind in range(index,len(nums)): #iterate over eveyr posisbility, can reuse natuarlly 
                currentValue=nums[ind]
                current.append(currentValue)
                backtrack(ind,currentSum+currentValue)
                current.pop()
            
        backtrack(0,0)
        return result

    #O(target/smallest vlaue * 2^target/samellst value) 
    #space O(target/smallest value)
            



                