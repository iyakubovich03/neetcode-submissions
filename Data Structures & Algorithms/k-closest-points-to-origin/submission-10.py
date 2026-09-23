import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for index,value in enumerate(points):
            x,y=value
            current=x**2+y**2
            heapq.heappush(heap,(-current,index))
            if len(heap)>k:
                heapq.heappop(heap)
        result=[]
        for _,index in heap:
            result.append(points[index])
        return result

        