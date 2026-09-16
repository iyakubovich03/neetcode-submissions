# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        h=0
        valR=None
        def pot(root):
            nonlocal h
            nonlocal valR
            if not root:
                return
            pot(root.left)# traverse all the way down to hteleft 
            h+=1
            if (h==k):
                valR=root.val
            pot(root.right)
        pot(root)
        return valR



        