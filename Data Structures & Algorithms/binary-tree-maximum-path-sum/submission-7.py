# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        globalMax=-float('inf')

        def dfs(current):
            nonlocal globalMax
            if not current:
                return 0

            left=dfs(current.left)
            right=dfs(current.right)

            value=max(current.val,current.val+left+right,current.val+left,current.val+right)
            globalMax=max(globalMax,value)
            return max(current.val,current.val+left,current.val+right)

        dfs(root)
        return globalMax
        