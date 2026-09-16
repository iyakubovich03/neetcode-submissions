import math
import heapq
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        for i in range(len(points)):
            a,b=points[i]
            dist=((a)**2+(b)**2)
            points[i]=[dist,a,b]
        #resets with distance 
        #run quickselect this acutally sorts n then arpiton
        def partition(arr,l,r):
            piv=arr[r][0]
            i=l
            for j in range(l,r):
                if arr[j][0]<=piv:
                    arr[j],arr[i]=arr[i],arr[j]#flips value
                    i+=1
            arr[r],arr[i]=arr[i],arr[r]#flips
            return i #return teh pivot location 

        def quickselect(arr,k,l,r):
            if l>=r:
                return
            ind=partition(arr,l,r)
            if ind-l+1>k:
                return quickselect(arr,k,l,ind-1)
            if ind-l+1==k:
                return 
            return quickselect(arr,k,ind+1,r)
        
        if len(points)==0 or k==0:
            return
        quickselect(points,k,0,len(points)-1)
        arr=[]
        for i in range(k):
            z,a,b=points[i]
            arr.append([a,b])
        return arr
            





        