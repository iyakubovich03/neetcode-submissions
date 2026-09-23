import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #create new array and just sort it nlogn n tkae subarray NLONGN
        #new array heap (klogk) j inverted w max
        #iterate again andappend 
        
        heap=[]
        for index,(x,y) in enumerate(points):
            current=x**2+y**2
            heapq.heappush(heap,(-current,index))

            if len(heap)>k:
                heapq.heappop(heap)

        return [points[index] for _,index in heap]
        