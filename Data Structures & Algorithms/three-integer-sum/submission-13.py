class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
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
        """
        sum_outputs=[]
        nums.sort() #the array is sorted nlog(n)
        for i in range(len(nums)-1):# property since sorted just skip repreate lements
            
            start=nums[i]
            total=0-start
            #now run left n right bound
            left=i+1
            right=len(nums)-1
            while left<right:
                tot= nums[left]+nums[right]#current sum
                if tot<total:
                    #iterate right
                    left+=1
                elif tot>total:
                    right-=1
                else:
                    if [nums[i],nums[left],nums[right]] not in sum_outputs:
                        sum_outputs.append([nums[i],nums[left],nums[right]])
                    
                    left+=1
                    while left>0 and left<len(nums) and nums[left]==nums[left-1]:
                        left+=1
            #this shoudl capture all the sums
        print(sum_outputs)
        return sum_outputs

                