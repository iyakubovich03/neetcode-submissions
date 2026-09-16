class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a=[]
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                tot=nums[l]+nums[r]+nums[i]
                if tot>0:
                    r-=1
                if tot<0:
                    l+=1
                if tot == 0:
                    if [nums[l],nums[r],nums[i]] not in a:
                        a.append([nums[l],nums[r],nums[i]])
                    l+=1

                    while(nums[l]==nums[l-1]) and l<r:
                        l+=1
        return a



        