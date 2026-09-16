# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:# base case empty
            return None
        #split segemnet up into two left sub tree n right subtree do this by obtianig the roort n getting the index in 
        #inorder from min to max
        #pre order root, then left subtree, then right tree 
        root=TreeNode(preorder[0])# creates the first node
        
        ind=inorder.index(preorder[0])# gets index of root
        root.left=self.buildTree(preorder[1:ind+1],inorder[0:ind])
        root.right=self.buildTree(preorder[ind+1:len(preorder)],inorder[ind+1:len(inorder)])

        return root


        

