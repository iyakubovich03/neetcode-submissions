class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        we want a path to the end with the minimum max seen
        we can use a heap (from current look at each direction and push the max(current,new),row,col
        once we pop add to visited no need to revisit 
        then once we reach end we return 

        """
        heap=[]
        heapq.heappush(heap,(grid[0][0],0,0))
        direction=[[-1,0],[1,0],[0,1],[0,-1]]
        visited=set()
        while heap:
            dist,r,c=heapq.heappop(heap)
            if (r,c) in visited: #potentially add several on already 
                continue
            if r==len(grid)-1 and c==len(grid[0])-1:
                return dist
            #look at each diretoin 
            visited.add((r,c))
            for dr,dc in direction:
                nr=dr+r
                nc=dc+c
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and (nr,nc) not in visited:
                    heapq.heappush(heap,(max(dist,grid[nr][nc]),nr,nc))
        return -1
                