# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        
        def pot(root,val):
            if not root:
                return None
            if len(res)==val:
                res.append([])
            
            res[val].append(root.val)
            pot(root.left,val+1)
            pot(root.right,val+1)
            
        pot(root,0)
        return res

      
        
            


        