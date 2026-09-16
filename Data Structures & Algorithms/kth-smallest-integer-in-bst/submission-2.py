# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        va=k
        po=None
        if not root:
            return None
        #IS THERE A WAY TO SORT AS WE ITERATE 
        def pot(root):
            nonlocal va
            nonlocal po
            if not root:
                return None
            pot(root.left)
            va-=1
            if va==0:
                po=root.val
                return
            pot(root.right)
        pot(root)
        
        return po



        