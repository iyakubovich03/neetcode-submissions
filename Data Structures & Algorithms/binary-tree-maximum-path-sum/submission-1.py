# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        h= -float('inf')# this will keep track of the max value 

        def rec(roo):
            nonlocal h
            if not roo:
                return 0
            l=max(rec(roo.left),0)# dfs just maxmizes
            r=max(rec(roo.right),0)# dfs just maximizes 
            h=max(h,l+r+roo.val) # already had it 
            return roo.val+max(l,r)
        rec(root)
        return h

            
            #recusive calls
            #is there a brute way of doing iterate over all nodes skippnig from each node tryign to maximize
