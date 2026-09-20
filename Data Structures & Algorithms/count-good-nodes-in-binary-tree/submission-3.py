# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes=0
        self.dfs(root,root.val)
        return self.goodNodes


    def dfs(self,current,value):
        if not current:
            return 

        if current.val>=value:
            self.goodNodes+=1
        
        self.dfs(current.left,max(value,current.left.val if current.left else float('inf')))
        self.dfs(current.right,max(value,current.right.val if current.right else float('inf')))

        return

        