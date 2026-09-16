class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if (i>0 and nums[i]==nums[i-1]):
                continue
            j=i+1
            r=len(nums)-1
            targ=0-nums[i]
            while j<r:
                if (nums[j]+nums[r]>targ):
                    r-=1
                elif (nums[j]+nums[r]<targ):
                    j+=1
                else:
                    res.append([nums[i],nums[j],nums[r]])
                    j+=1
                    while j<r and nums[j]==nums[j-1]:
                        j+=1
        print(res)
        return res

                