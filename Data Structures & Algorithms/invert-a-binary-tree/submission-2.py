# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q=[]
        q.append(root)
        while q:
            val=q.pop(0)
            l=val.left
            r=val.right# gets vals 
            val.left=r #flips
            val.right=l#flips 
            if r: 
                q.append(r)
            if l: 
                q.append(l)
        return root
           
            
        

            


        