# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #values here are ordered 
        val1=root
        while val1:
            if val1.val>p.val and val1.val>q.val:#shfitng
                val1=val1.left
            elif val1.val<p.val and val1.val<q.val:#shifitng
                val1=val1.right
            else:
                break
           
        return val1
      