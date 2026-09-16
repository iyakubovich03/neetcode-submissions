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
        if not subRoot:
            return True
        if not root:
            return False
        
        def pot(rot,subR):# basic subtree checking
            if not rot and not subR:
                return True
            if not rot or not subR or rot.val!=subR.val:
                return False
            return pot(rot.left,subR.left) and pot(rot.right,subR.right)
        return pot(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)