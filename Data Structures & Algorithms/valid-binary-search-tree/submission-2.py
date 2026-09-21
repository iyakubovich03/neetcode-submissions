# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #each left subtree 
        return self.dfs(root,-float('inf'),float('inf'))
        

    def dfs(self,current,leftLimit,rightLimit):
        if not current:
            return True
        
        return leftLimit<current.val<rightLimit and self.dfs(current.left,leftLimit,current.val) and self.dfs(current.right,current.val,rightLimit)