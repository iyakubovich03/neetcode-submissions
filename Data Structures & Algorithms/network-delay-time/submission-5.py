import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    
        """
        adjList={} mapping source to (time,target)
        heap=[]
        put on children of adjList[k] onto heap
        we will store a shared seen state
        then enter while loop, pop of heap and push on to heap prevTime+duration onto heap
        if while loop if len(seen)==n: return duration 

        otherwise return -1

        O(V+E)+ (V+E)Log(V+E) time space: O(V+E)
        """
        adjList=defaultdict(list)
        for source,target,time in times:
            adjList[source].append((time,target))
        heap=[]
        for time,target in adjList[k]:
            heapq.heappush(heap,(time,target))
        visited={k}
        while heap:
            
            timeTook,source=heapq.heappop(heap)
            if source in visited:
                continue
            visited.add(source)
            if len(visited)==n: #in the case this never goes off heap might have extra
                return timeTook
            for time,target in adjList[source]:
                if target not in visited:
                    heapq.heappush(heap,(timeTook+time,target))
        return -1



        


        