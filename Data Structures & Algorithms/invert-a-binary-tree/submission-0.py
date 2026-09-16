# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q = []
        q.append(root)
        while(q):
            t=q.pop(0)
            t.left,t.right=t.right,t.left
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        return root
            


        