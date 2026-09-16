class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        final=[]
        for i in range(len(nums)-1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            targ=0-nums[i]
            while (l<r):
                
                if nums[l]+nums[r]>targ:
                    r-=1
                elif nums[l]+nums[r]<targ:
                    l+=1
                else:
                    final.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while (l<r and nums[l]==nums[l-1]):
                        l+=1

        return final