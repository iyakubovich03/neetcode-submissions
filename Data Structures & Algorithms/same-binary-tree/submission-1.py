# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        po=[]
        to=[]
        po.append(p)
        to.append(q)
        while po and to:
            val1=po.pop(0)
            val2=to.pop(0)
            if not val1 and not val2:
                continue
            if not val1 or not val2:
                return False
            if val1.val!=val2.val:
                return False
            po.append(val1.left)
            po.append(val1.right)
            to.append(val2.left)
            to.append(val2.right)
        return True
            




           

        