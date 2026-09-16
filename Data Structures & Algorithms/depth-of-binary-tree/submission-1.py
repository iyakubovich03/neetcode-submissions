# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=[]
        retV=0
        q.append([root,1])
        while q:
            l,height=q.pop(0)
            retV=max(retV,height)
            if l.left:
                q.append([l.left,height+1])
            if l.right:
                q.append([l.right,height+1])
        return retV
        
       