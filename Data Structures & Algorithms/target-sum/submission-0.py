class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        operations=[-1,1] #either add or subtract 

        def dfs(index,current_sum):

            if index==len(nums) and current_sum==target:
                return 1
            elif index==len(nums):
                return 0#not viable 

            #the current sum depends on on the previous chosen values
            if (index,current_sum) in memo:
                return memo[(index,current_sum)] #number of unique ways from index,current sum
            valid_ways=0
            for operation in operations:
                valid_ways+=dfs(index+1,current_sum+operation*nums[index])

            memo[(index,current_sum)]=valid_ways
            return memo[(index,current_sum)]
        
        return dfs(0,0)

        #at each index we can either add or subtract (2 decisiosn) 
        #we must use all teh values 
        #if we reach the same index and sum we dont have to repeat work 
        # n*current_sum  cases 
        # n*current_sum


        