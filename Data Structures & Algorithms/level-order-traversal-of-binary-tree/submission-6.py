# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[]
        final=[]
        q.append(root)
        if not root:
            return []
        while q:
            i=len(q)
            result=[]
            for j in range(i):
                val=q.pop(0)
                result.append(val.val)
                if val.left:
                    q.append(val.left)
                if val.right:
                    q.append(val.right)
            final.append(result)
        return final

        