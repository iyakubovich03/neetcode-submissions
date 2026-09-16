# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = []
        count = 0

        q.append([root, -float('inf')])  # Start with negative infinity as max
        while q:
            curr, max_val = q.pop(0)  # `max` is a reserved function, so rename it
            if curr.val >= max_val:
                count += 1
                max_val = max(curr.val,max_val)
                  # Update max value
            
            if curr.left:
                q.append([curr.left, max_val])  # Pass updated max
            if curr.right:
                q.append([curr.right, max_val])  # Pass updated max

        return count

       