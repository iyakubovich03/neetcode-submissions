class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        current=[]
        #missing 

        def backTrack(index):
            if index==len(nums):
                result.append(current.copy())
                return
            
            #take the current Value case
            currentValue=nums[index]
            current.append(currentValue)
            backTrack(index+1)
            current.pop()

            backTrack(index+1)
            return 

        

        backTrack(0)
        return result