# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0 
            leftSide=dfs(root.left)
            rightSide=dfs(root.right)
            maxDiameter[0]=max(maxDiameter[0],leftSide+rightSide)
            return max(leftSide,rightSide)+1

        maxDiameter=[0]
        dfs(root)
        return maxDiameter[0]

       




        