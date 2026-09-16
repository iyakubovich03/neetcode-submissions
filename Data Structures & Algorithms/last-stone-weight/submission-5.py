import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #quick solution, sort the array array put it into a stack, pop every 2 while length is 2, and do compariosn add back
        stones=[-s for s in stones]#takes msalelst 
        heapq.heapify(stones)
        #heappush
        #heappop

        
        print(stones)
        while len(stones)>1:
            val1=heapq.heappop(stones)
            val2=heapq.heappop(stones)
            if val1<val2:
                heapq.heappush(stones,-(val2-val1))
            print(stones)
        
        return abs(stones[0]) if stones else 0
        
            #do this until length oen 
        

