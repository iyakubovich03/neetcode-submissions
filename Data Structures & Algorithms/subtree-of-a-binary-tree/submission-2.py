# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.pot(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def pot(self,roo,tre):
            if not roo and not tre:
                return True
            if roo and tre and roo.val==tre.val:
                return self.pot(roo.left,tre.left) and self.pot(roo.right,tre.right)
            return False
        

        
