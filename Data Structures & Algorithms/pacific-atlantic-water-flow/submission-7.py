from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #BRUTE FORCE (row*col)*(row*col) Space: #number of solutions
        #(Row * Col) + O(Row*Col)*2
        pacificVisited=set()
        atlanticVisited=set()
        directions=[[0,1],[0,-1],[-1,0],[1,0]]

        def dfs(row,col,seen):
            seen.add((row,col))
            currentValue=heights[row][col]

            for dr,dc in directions:
                nr=row+dr
                nc=col++dc
                if (nr,nc) not in seen and 0<=nr<len(heights) and 0<=nc<len(heights[0]) and currentValue<=heights[nr][nc]:
                    dfs(nr,nc,seen)

        for col in range(len(heights[0])):
            if (0,col) not in pacificVisited:
                dfs(0,col,pacificVisited)
            if (len(heights)-1,col) not in atlanticVisited:
                dfs(len(heights)-1,col,atlanticVisited)
            #directly invoke the dfs
        
        for row in range(len(heights)):
            if (row,0) not in pacificVisited:
                dfs(row,0,pacificVisited)
            if (row,len(heights[0])-1) not in atlanticVisited:
                dfs(row,len(heights[0])-1,atlanticVisited)

        return list(pacificVisited & atlanticVisited)
            
        #O(row*col) +2*(row*col) space (row*col)
        