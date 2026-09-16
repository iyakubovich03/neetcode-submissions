# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def pot(curr,ti):
            nonlocal count
            if not curr:
                return None
            if (curr.val>=ti):
                count+=1
                ti=curr.val
            pot(curr.left,ti)
            pot(curr.right,ti)
        pot(root,-float('inf'))
        return count

       