import math
import heapq
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #given a set of points
        #you need to calculate the distnace 
        #flip teh distance to negative n pop len-k times
        #should have an array filled with the weights 


        #interpeted wrong, basiclly you want to return the k closest points(smilar to bf you want to pop off the heap until you have the k clsoest points)
        #filled w array dista=[]
        dista=[]
        for i in range(len(points)):
            a,b=points[i]
            dist=math.sqrt(((a)**2+(b)**2))
            dista.append([-dist,[a,b]])
        print(dista)
        heapq.heapify(dista)
        for i in range(len(points)-k):
            heapq.heappop(dista)
        #the reaminig are valid 
        
        res=[]
        for a,b in dista:
            res.append(b)
        print(f"should reflect associated distances now")
        print(dista)
        return res
       
    
        