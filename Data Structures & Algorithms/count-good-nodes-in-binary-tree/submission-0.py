# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        track=0
        def pot(root,val):
            nonlocal track

            if not root:
                return None
            if root.val>=val:
                track+=1
            val=max(val,root.val)
            pot(root.left,val)
            pot(root.right,val)
        pot(root,-10000)
        return track