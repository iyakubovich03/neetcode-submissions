# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def pot(root):

            if not root:
                return 0 
            l=pot(root.left)
            r=pot(root.right)
            return max(l,r)+1
        return pot(root)
        
       