class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #first pass iterate to the end n just mulitply 
        result=[1]*len(nums)
        for index in range(len(nums)-1):
            result[index+1]*=nums[index]*result[index]
        #now we take current 
        current=1
        for index in range(len(nums)-1,0,-1):
            current*=nums[index]
            result[index-1]*=current
        return result        
        