class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we are looking for the mid
        l,r=0,len(nums)-1
        def recurse(left,right,arr):
            if arr[left]<=arr[right]: #base that is sorted
                return arr[left]

            mid=left+(right-left)//2
            if arr[mid]<arr[mid-1]:
                return arr[mid]
            if arr[mid]>arr[mid+1]:
                return arr[mid+1]

            if arr[mid]<arr[left]:
                return recurse(left,mid-1,arr)
            else:
                return recurse(mid+1,right,arr)
        return recurse(l,r,nums)
