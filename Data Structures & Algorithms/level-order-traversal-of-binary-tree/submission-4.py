# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        l=[]
        if not root:
            return []
        l.append(root)
        
        while l:
            le=len(l)
            level=[]
            for i in range(le):
                val=l.pop(0)
                if val.left:
                    l.append(val.left)
                if val.right:
                    l.append(val.right)
                level.append(val.val)
            res.append(level)
        return res
        
            


        