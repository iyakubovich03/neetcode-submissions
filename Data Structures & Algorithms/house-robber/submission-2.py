class Solution:
    def rob(self, nums: List[int]) -> int:
        #you want to maximize the sum but you must make sure that you there are no adjacent
        #values
        #idea we recruse to non adjacent neighbors and test it out
        #if i wasnt tracking 
        
        track=[-1 for i in range(len(nums))]
        def pot(index):
            nonlocal track
            if index>=len(nums):
                return 0
            if track[index]!=-1:
                return track[index]
            val1=pot(index+1)
            val2=nums[index]+pot(index+2)
            track[index]=max(val1,val2)
            return max(val1,val2)
        #now we want to retunr ht emax of hte array 
      
        if not nums:
            return 0
        
        return pot(0)