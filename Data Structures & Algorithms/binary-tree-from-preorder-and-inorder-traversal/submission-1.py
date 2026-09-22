# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inOrderMap={} # value : index
        for index,value in enumerate(inorder):
            inOrderMap[value]=index

        self.currentPointer=0

        def dfs(low,high):
            if high<low:
                return None

            currentValue=preorder[self.currentPointer]
            self.currentPointer+=1
            #now we split 
            left=dfs(low,inOrderMap[currentValue]-1)
            right=dfs(inOrderMap[currentValue]+1,high)
            
            currentNode=TreeNode(currentValue,left,right)
            return currentNode       

        return dfs(0,len(preorder)-1) 

# [1,2,3,4] : pre
# [2,1,3,4]: inorder

#
#{2:0,1:1,3:2,4:3}

#dfs(0,3). #(1).  left: (1,1).  right: (2,3)
#Node (2).  left (1,0) right (2,1)
#both return None None
#(2,3) currentNode(3), (2,1) ((3,3))
#left None
#right node (3)





    """

    pre order

    add(value)
    dfs(curr.left)
    dfs(curr.right)

    """


    """
    in order

    dfs(curr.left)
    add(value)
    """