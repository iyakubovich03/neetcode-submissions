# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root,-float('inf'))


    def dfs(self,current,value):
        if not current:
            return 0

        leftSide=self.dfs(current.left,max(value,current.val))
        rightSide=self.dfs(current.right,max(value,current.val))

        if current.val>=value:
            return leftSide+rightSide+1

        return leftSide+rightSide

        
            #increment by 1 



        return

        