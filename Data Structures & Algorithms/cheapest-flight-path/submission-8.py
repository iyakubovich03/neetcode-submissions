class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs=[float('inf')]*n #dp, cheapest flight to get to this stae
        costs[src]=0#base 
        for _ in range(k+1):
            #we dont want newly update distances to affect the new ones (only want to expadn one edge at a time
            temp=costs.copy()
            for source,destination,price in flights:# O(V+E)
                if costs[source]!=float('inf'):
                    temp[destination]=min(temp[destination],costs[source]+price)
            costs=temp
        return costs[dst] if costs[dst]!=float('inf') else -1
        
    

            