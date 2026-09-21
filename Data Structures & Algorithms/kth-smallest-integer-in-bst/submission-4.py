# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.value=None
        self.k=k
        self.current=0
        self.dfs(root)
        return self.value



    def dfs(self,current):
        if not current:
            return
        leftSide=self.dfs(current.left)
        self.current+=1
        if self.current==self.k:
            self.value=current.val
        rightSide=self.dfs(current.right)
        return
        
        