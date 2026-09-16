from collections import deque,defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        track=defaultdict(int)
        for a in tasks:
            track[a]-=1
        #opoulated 
        val=list(track.values())# holds the frequency
        heapq.heapify(val)
        que=deque()
        current=0
        while que or val:
            current+=1
            if val:#not empty
                curr=heapq.heappop(val)+1
                if curr:#not 0 
                    que.append([curr,current+n])
            if que:
                value,time=que[0]
                if time==current:
                    que.popleft()
                    heapq.heappush(val,value)			
        return current

