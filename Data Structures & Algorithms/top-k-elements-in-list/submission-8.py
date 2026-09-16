import numpy as np
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        track={}
        arr=[]
        for i in nums:
            track[i]=track.get(i,0)+1 #tracks frequency 
          
        t=[]
        #filled up track with number 
        for val,key in track.items():
            arr.append([key,val])
        arr.sort()
        arr=arr[::-1]

        ind=0
        while k>0:
            t.append(arr[ind][1])
            ind+=1
            k-=1
        return t
            
            
