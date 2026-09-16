class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        res=nums[0]
        while l<=r:
            if nums[l]<nums[r]: #originally to check if array is alreayd sorted if it is it will break the loop n give the value of the min
                res=min(res,nums[l])
                break
            mid=(l+r)//2 
            res=min(res,nums[mid]) # it will continously check if ecah val is more min
            if (nums[mid]>=nums[l]): #checking mid to see if it is greater than left val if is keep going till its not 
                l=mid+1
            else:  #if not greater or eqaul n less it will move left till right and left they cross n it will reutnr res
                r=mid-1
        return res