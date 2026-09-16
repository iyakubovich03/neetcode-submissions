# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def pot(typ):
            if typ is None:
                return 0
            l=pot(typ.left)#will go all way down n recurse back up, these r computed
            r=pot(typ.right)#goes all way down n recrusers back up

            if l==-1 or r==-1:
                return -1 #so this is the case that we already know its unbalnaced j contineus reseting to -1 propogrates up
            if abs(l-r)>1:
                return -1


            return 1+max(l,r)# this claculates the current hiehgt for that current node
        return pot(root)!=-1

        