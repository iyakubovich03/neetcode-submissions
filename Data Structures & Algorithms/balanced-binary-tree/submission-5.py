# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _,balanced=self.dfs(root)
        return balanced


    def dfs(self,current):
        if not current:
            return 0,True

        leftSide,balancedL=self.dfs(current.left)
        rightSide,balancedR=self.dfs(current.right)

        if not balancedL or not balancedR or abs(leftSide-rightSide)>1:
            return 0,False
        
        return max(leftSide,rightSide)+1, True

        