# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def potato(root):
            if not root:
                return [True,0]
            left,right=potato(root.left),potato(root.right)
            bal= left[0] and right[0] and (abs(left[1]-right[1])<=1)
            return [bal,1+max(left[1],right[1])]
       
        return potato(root)[0]