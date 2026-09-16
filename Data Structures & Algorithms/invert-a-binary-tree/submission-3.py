# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
    
        def pot(root):
            if not root:
                return None
            x=root.left
            root.left=pot(root.right)
            root.right=pot(x)

            return root
        
        return pot(root)
                
            

            


        