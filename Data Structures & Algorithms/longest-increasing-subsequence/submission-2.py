class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr=[1]*len(nums)

        for index in range(len(nums)):
            for index2 in range(index+1,len(nums)):
                value1=nums[index]
                value2=nums[index2]
                if value2>value1:
                    arr[index2]=max(arr[index2],arr[index]+1)
        print(arr)        
        return max(arr)
        