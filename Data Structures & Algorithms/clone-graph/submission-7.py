"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        memo={}
        def dfs(reference):
            if not reference:
                return None
            if reference.val in memo:
                return memo[reference.val]
            
            #otherwise we will create it 
            memo[reference.val]=Node(reference.val)
            for neighbor in reference.neighbors:
                memo[reference.val].neighbors.append(dfs(neighbor))

            return memo[reference.val]

        return dfs(node)

        