# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        va=[]
        if not root:
            return None
        
        def pot(root):
            nonlocal va
            if not root:
                return None
            if root.val not in va:
                va.append(root.val)
            pot(root.left)
            pot(root.right)
        pot(root)
        va=sorted(va)
        return va[k-1]



        