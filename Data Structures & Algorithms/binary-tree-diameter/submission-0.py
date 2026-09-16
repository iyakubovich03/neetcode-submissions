# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        h=0
        def pot(root):
            nonlocal h
            if not root:
                return 0
            l=pot(root.left)
            r=pot(root.right)
            h=max(h,l+r)
            return 1+max(l,r)
        pot(root)
        return h

        