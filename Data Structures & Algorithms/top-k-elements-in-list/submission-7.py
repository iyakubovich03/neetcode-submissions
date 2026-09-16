import numpy as np
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        track={}
        arr=[[]]*(len(nums)+1)
        for i in nums:
            track[i]=track.get(i,0)+1
          
        t=[]
        #filled up track with number 
        for val,key in track.items():
            arr[key]=arr[key]+[val]
        for i in range(len(arr)-1,0,-1):
            if not arr[i]:
                continue
            for j in arr[i]:
                k-=1
                t.append(j)
                if(k<=0):
                    return t
        
            
