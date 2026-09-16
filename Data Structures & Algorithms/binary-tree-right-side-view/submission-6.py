# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        typ=[]
        typ.append(root)
        while typ:
            le=len(typ)
            for i in range(le):
                temp=typ.pop(0)
                if not temp:
                    continue
                if (i==le-1):
                    res.append(temp.val)
                if temp.left:
                    typ.append(temp.left)
                if temp.right:
                    typ.append(temp.right)
        return res
                
