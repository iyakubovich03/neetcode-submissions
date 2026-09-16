class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findRotatedIndex():
            l,r=0,len(nums)-1
            while l<r:
                mid=l+(r-l)//2
                if nums[mid]<nums[-1]:
                    r=mid
                else:
                    l=mid+1
            return l
        
        def binarySearch(l,r):
            while l<=r:
                mid=l+(r-l)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return -1
        rotatedIndex=findRotatedIndex()
        if not rotatedIndex:
            return binarySearch(0,len(nums)-1)
        if nums[0]<=target<=nums[rotatedIndex-1]:
            return binarySearch(0,rotatedIndex-1)
        else:
            return binarySearch(rotatedIndex,len(nums)-1)

