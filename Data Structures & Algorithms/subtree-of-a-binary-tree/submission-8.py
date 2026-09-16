# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        candidates=[]
        #O(N)
        def dfs(root):
            if not root:
                return
            if root.val==subRoot.val:
                candidates.append(root)
            dfs(root.left)
            dfs(root.right)
        dfs(root)

        for candidate in candidates:
            if self.isSameTree(candidate,subRoot):
                return True
        return False


    #O(min(subRoot,tree))
    def isSameTree(self,p,q):
        if not p and not q:
            return True
        elif not p and q or not q and p:
            return False
        if p.val!=q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        