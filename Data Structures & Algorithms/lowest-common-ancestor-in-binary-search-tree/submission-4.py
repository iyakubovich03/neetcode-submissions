# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val<=root.val<=q.val or q.val<=root.val<=p.val :
            return root

        value=None
        if root.val>p.val and root.val>q.val:
            value=self.lowestCommonAncestor(root.left,p,q)
        else:
            value=self.lowestCommonAncestor(root.right,p,q)
        return value

        



        """
        deq=deque([root])
        if p.val>q.val:
            p,q=q,p

        while deq:
            current=deq.popleft()

            if p.val<=current.val<=q.val:
                return current

            if current.val>p.val and current.val>q.val:
                deq.append(current.left)
            else:
                deq.append(current.right)
            """


        