class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #run quickselect but 
        #run fastselect most optimal 
        def partition(arr,l,r):
            pivot=arr[r]
            i=l
            for j in range(l,r):
                if arr[j]<=pivot:
                    arr[j],arr[i]=arr[i],arr[j]#makes sure before pivot
                    i+=1
            #at end must flip pivot with r 
            arr[r],arr[i]=arr[i],arr[r]
            return i#we retunr the index of the pivot
        def quickselect(arr,l,r,k):
            index=partition(arr,l,r)
            if l>=r:
                return index
            if index-l+1==k:
                return index
            if index-l+1>k:
                return quickselect(arr,l,index-1,k)
            #else
            return quickselect(arr,index+1,r,k-(index-l+1))

        #kth largest elmeent in teh array is len(nums)-k

        return nums[quickselect(nums,0,len(nums)-1,len(nums)-k+1)] if nums else None