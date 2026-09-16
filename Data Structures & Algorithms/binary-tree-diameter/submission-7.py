# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxDiameter=[0]
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.maxDiameter[0]

    def dfs(self,root):
        if not root:
            return 0 

        leftSide=self.dfs(root.left)
        rightSide=self.dfs(root.right)
        print(f"current leftSide value: {leftSide}")
        print(f"current rightSide value: {rightSide}")
        self.maxDiameter[0]=max(self.maxDiameter[0],leftSide+rightSide)
        print(f"this is the current width at node: {root.val} size: {leftSide+rightSide}, my neighrbors are left: {root.left} and right: {root.right}")
        print(f"current max diameter {self.maxDiameter[0]}")
        

        return max(leftSide,rightSide)+1




        