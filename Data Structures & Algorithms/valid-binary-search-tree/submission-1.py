# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def pot(roo,lower,higher):
            if not roo:
                return True # base case

            if (not (lower<roo.val<higher)):
                return False

            return pot(roo.left,lower,roo.val) and pot(roo.right,roo.val,higher) #this is the pattern
        return pot(root,-float('inf'),float('inf'))


          #perhaps maintain a lcoal max n min for left n right 

