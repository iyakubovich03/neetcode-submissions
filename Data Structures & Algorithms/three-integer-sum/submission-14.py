class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for index in range(len(nums)-2):
            current=nums[index]
            if index>0 and current==nums[index-1]:
                continue
            l=index+1
            r=len(nums)-1
            while l<r:
                leftSide,rightSide=nums[l],nums[r]
                if leftSide+rightSide+current==0:
                    result.append([current,leftSide,rightSide])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif nums[l]+nums[r]+current>0:
                    r-=1
                else:
                    l+=1
        return result


        