# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        rowMap=defaultdict(list)
        def dfs(current,row):
            if not current:
                return
            
            rowMap[row].append(current.val)
            dfs(current.left,row-1)
            dfs(current.right,row-1)

        dfs(root,0)
        
        return list(rowMap.values())
        













        """
        if not root:
            return []
        deq=deque([root])
        result=[]

        while deq:
            current=[]
            for _ in range(len(deq)):
                currentNode=deq.popleft()
                current.append(currentNode.val)
                if currentNode.left:
                    deq.append(currentNode.left)
                if currentNode.right:
                    deq.append(currentNode.right)
            result.append(current)
        return result
        """

        