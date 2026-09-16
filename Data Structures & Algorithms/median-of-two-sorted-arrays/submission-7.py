class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=nums1+nums2
        l=sorted(l)
        x=len(l)//2
        if len(l)==0:
            return 0
        
      
        if len(l) %2 ==0:
         
            return (l[x]+l[x-1])/2
        else:
     
            return l[x]