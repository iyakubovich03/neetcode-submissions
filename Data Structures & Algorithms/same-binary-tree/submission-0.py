# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l=[]
        r=[]
       
        l.append(p)
        r.append(q)
        while l and r:
            lA=l.pop(0)
            rA=r.pop(0)
            if not lA and not rA:
                continue
            
            if not lA or not rA or lA.val!=rA.val:
                return False

            l.append(lA.left)
            l.append(lA.right)
            r.append(rA.left)
            r.append(rA.right)
        return True


           

        