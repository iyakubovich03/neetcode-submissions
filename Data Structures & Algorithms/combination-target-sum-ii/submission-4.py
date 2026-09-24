class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result=[]
        currentValues=[]
        currentSum=0
        candidates.sort()
        #reminds of 3 sum when we see biggest value we only need to consdier this
        def backtrack(index):
            nonlocal currentSum

            if currentSum==target:
                result.append(currentValues.copy())
                return
            
            if currentSum>target or index==len(candidates):
                return

            #we want the first layer
            for ind in range(index,len(candidates)):

                if ind>index and candidates[ind]==candidates[ind-1]:
                    continue # we are not looping on this vlaue 

                value=candidates[ind]
                currentValues.append(value)
                currentSum+=value
                backtrack(ind+1)
                #get rid of those values
                currentSum-=value
                currentValues.pop()
          

       
        backtrack(0)
        return result
        