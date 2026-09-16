# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        final=[]
        q=[]
        q.append(root)
        
        if not root:
            return []
        while q:
            t=len(q)
            for i in range(t):
                curr=q.pop(0)
                if i==t-1:
                    final.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
        return final