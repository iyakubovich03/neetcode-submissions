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
        good=1 if current.val>=value else 0
        maxSoFar=max(value,current.val)
        return self.dfs(current.left,max(value,current.val))+self.dfs(current.right,max(value,current.val))+good
    


    # can also do this withh bfs just use a tuple to track previous max
    # O(N) #O(height of tree)


        