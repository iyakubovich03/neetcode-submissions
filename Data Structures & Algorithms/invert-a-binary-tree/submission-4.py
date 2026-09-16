# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        deq=deque([root])
        while deq:
            currentNode=deq.popleft()
            leftNode=currentNode.left
            rightNode=currentNode.right
            currentNode.right=leftNode
            currentNode.left=rightNode
            if leftNode:
                deq.append(leftNode)
            if rightNode:
                deq.append(rightNode)
        return root

        