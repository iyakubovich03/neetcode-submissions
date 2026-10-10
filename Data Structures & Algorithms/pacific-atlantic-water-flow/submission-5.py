from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #BRUTE FORCE (row*col)*(row*col) Space: #number of solutions
        #(Row * Col) + O(Row*Col)*2
        pacificVisited=set()
        atlanticVisited=set()
        directions=[[0,1],[0,-1],[-1,0],[1,0]]

        def dfs(row,col,seen):
            currentValue=heights[row][col]
            for dr,dc in directions:
                nr=row+dr
                nc=col++dc
                if (nr,nc) not in seen and 0<=nr<len(heights) and 0<=nc<len(heights[0]) and currentValue<=heights[nr][nc]:
                    print(f"current exploring from ({row},{col})now looking at ({nr},{nc})")
                    seen.add((nr,nc))
                    dfs(nr,nc,seen)

        for col in range(len(heights[0])):
            pacificVisited.add((0,col))
            atlanticVisited.add((len(heights)-1,col))
            dfs(0,col,pacificVisited)
            dfs(len(heights)-1,col,atlanticVisited)
            #directly invoke the dfs
        
        for row in range(len(heights)):
            pacificVisited.add((row,0))
            atlanticVisited.add((row,len(heights[0])-1))
            
            dfs(row,0,pacificVisited)

            dfs(row,len(heights[0])-1,atlanticVisited)
        print(f"pacific visited {pacificVisited}")
        print(f"ataltnic Visited {atlanticVisited}")

        return list(pacificVisited & atlanticVisited)
            
        #reachable cells from pacific
        #rechabel cells from atalntic 
        #intersection of these cells converted to a list 
        #dont want to reiterate on cells already visited so keep tracked cells viisted

