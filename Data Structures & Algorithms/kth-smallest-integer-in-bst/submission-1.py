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
        #IS THERE A WAY TO SORT AS WE ITERATE 
        def pot(root):
            nonlocal va
            if not root:
                return None
            pot(root.left)
            if root.val not in va:
                va.append(root.val)
            pot(root.right)
        pot(root)
        
        return va[k-1]



        