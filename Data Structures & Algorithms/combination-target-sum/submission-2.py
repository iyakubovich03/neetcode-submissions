class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        current=[]
        currentSum=0

        def backtrack(index):
            nonlocal currentSum

            if currentSum>target: #greater bad
                return

            if currentSum==target: #equal good
                result.append(current.copy())
                return

            if index==len(nums): # over stop
                return

            #take current value 
            currentValue=nums[index]
            currentSum+=currentValue
            current.append(currentValue)

            #recruse on same index
            backtrack(index)

            #pop off n get rid of value
            current.pop()
            currentSum-=currentValue
            backtrack(index+1) #move forward

        backtrack(0)
        return result


            



                