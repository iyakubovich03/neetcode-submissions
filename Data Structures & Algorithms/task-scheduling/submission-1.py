from collections import defaultdict,deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency=defaultdict(int)
        heap=[]

        for t in tasks:
            frequency[t]+=1

        for key,value, in frequency.items():
            heapq.heappush(heap,(-value,key))

        deq=deque()
        
        totalTime=0
        while deq or heap:
            if not heap:
                totalTime=deq[0][0] #when its ready
                time,value,freq=deq.popleft()
                heapq.heappush(heap,(freq,value))

            freq,key=heapq.heappop(heap)
            

            if freq+1!=0:
                deq.append((totalTime+n+1,key,freq+1))

            totalTime+=1
            
            while deq and totalTime>=deq[0][0]: #inclusive
                time,value,freq=deq.popleft()
                heapq.heappush(heap,(freq,value))
            #when do we increment the time 

            
        return totalTime

            
    #X,2. (1).Y,3 2
        