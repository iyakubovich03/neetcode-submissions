# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return []
        val=0
        l=[]
        l.append(root)
        while l:
            tot=[]
            lent=len(l)
            for i in range(len(l)):
                nod=l.pop(0)
                if not nod:
                    continue
                    
                tot.append(nod.val)
                l.append(nod.left)
                l.append(nod.right)
            if tot:
                res.append(tot)
        return res    

      
        
            


        