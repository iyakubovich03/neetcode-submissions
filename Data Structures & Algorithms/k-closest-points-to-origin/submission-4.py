import math
import heapq
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dista=[]
        for i in range(len(points)):
            a,b=points[i]
            dist=-((a)**2+(b)**2)
            heapq.heappush(dista,[dist,a,b])
            if len(dista)>k:
                heapq.heappop(dista)#once over k will pop the biggest ones 
       
        res=[]
        for dist,a,b in dista:
            res.append([a,b])
        print(f"should reflect associated distances now")
        print(dista)
        return res
       
    
        