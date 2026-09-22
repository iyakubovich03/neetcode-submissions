# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        globalMax=-float('inf')

        def dfs(current): #O(N) time O(H) space
            nonlocal globalMax
            if not current:
                return 0

            left=dfs(current.left)
            right=dfs(current.right)

            value=max(current.val,current.val+left,current.val+right) #consider both,or singular, both ways)
            globalMax=max(globalMax,value,current.val+left+right)
            return value

        dfs(root)
        return globalMax
        