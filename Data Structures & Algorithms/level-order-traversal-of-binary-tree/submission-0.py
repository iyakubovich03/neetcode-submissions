# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]

        def pot(roo,val):
            if not roo:
                return None
            if val==len(res):
                res.append([])
            res[val].append(roo.val)
            pot(roo.left,val+1)
            pot(roo.right,val+1)

        pot(root,0)
        return res
      
        
            


        