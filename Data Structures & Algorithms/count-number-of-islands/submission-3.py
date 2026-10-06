from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction=direction=[[0,-1],[0,1],[1,0],[-1,0]]
        def dfs(row,col):
            for dr,dc in direction:
                nr=row+dr
                nc=dc+col
                if (nr,nc) not in visited and 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]=="1":
                    visited.add((nr,nc))
                    dfs(nr,nc)
        


        
        visited=set()
        total=0

        def bfs(row,col):
            deq=deque()
            deq.append((row,col))
            direction=[[0,-1],[0,1],[1,0],[-1,0]]
            while deq:
                row,col=deq.popleft()

                for dr,dc in direction:
                    nr=row+dr
                    nc=col+dc
                    if (nr,nc) not in visited and 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]=="1":
                        visited.add((nr,nc))
                        deq.append((nr,nc))
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c]=="1":
                    total+=1
                    visited.add((r,c))
                    dfs(r,c)
        return total 
        
        