class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bin(l,u,target,arr):
            if l>u:
                return -1
            mid=l+(u-l)//2
            if arr[mid]==target:
                return mid
            if arr[mid]>target:
                return bin(l,mid-1,target,arr)
            else:
                return bin(mid+1,u,target,arr)
        return bin(0,len(nums)-1,target,nums)
            