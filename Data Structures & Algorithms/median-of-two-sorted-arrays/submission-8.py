class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        total=len(nums1)+len(nums2)
        half=(total+1)//2

        l,r=0,len(nums1)
        while l<=r:
            mid=l+(r-l)//2 #2
            rest=half-mid

            smallerCurrent=nums1[mid-1] if mid>0 else -float('inf')
            smallerRight=nums1[mid] if mid<len(nums1) else float('inf')
            biggerCurrent=nums2[rest-1] if rest>0 else -float('inf')
            biggerRight=nums2[rest] if rest<len(nums2) else float('inf')

            if smallerCurrent<=biggerRight and biggerCurrent<=smallerRight:
                #if odd then return bigger of current
                if total%2:
                    return max(biggerCurrent,smallerCurrent)
                else:
                    return (max(biggerCurrent,smallerCurrent)+min(smallerRight,biggerRight))/2
            elif biggerCurrent>smallerRight:
    
                l=mid+1
            else:
                r=mid-1
        

        