# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #we can run the is same treeonce we reach taht ndoe 
        #first find if the subroot node is in the root
        #if it is then run a subtree method on it
        #if not return false
        if not root:
            return False
        def sub(root,subR):
            if not root and not subR:
                return True
            if not root or not subR or subR.val!=root.val:
                return False
            return sub(root.left,subR.left) and sub(root.right,subR.right)
        return sub(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)