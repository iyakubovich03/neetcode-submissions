# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # three condtions if reaches leaf then traverse back wont activat early
            return True
        if not p or not q:# if one is null n other isnt return false
            return False
        if p.val!=q.val: #if one doesnt eqaul other
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) # call recfusive checks agaisnt each node position same postion 

        #doesnt have to check for length but these ar ethe condiotins 
            




           

        