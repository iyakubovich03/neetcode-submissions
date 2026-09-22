# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        values=[]
        def dfs(root):
            if not root:
                values.append("None")
                return
            values.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        string="#".join(values)
        print(string)
        return string
        
        
    

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values=data.split("#") if data else []
        globalCounter=0
        def dfs():
            nonlocal globalCounter
            if globalCounter>=len(values):
                return None #might not need this
            currentValue=values[globalCounter]
            globalCounter+=1
            if currentValue=="None":
                return None
            left=dfs()
            right=dfs()
            obj=TreeNode(int(currentValue),left,right)
            return obj

        return dfs()

            

        
 
#ideas:
# mayb create a astring from bfs and append vlaues like Left,Right to it 

# 1L2R3L4R5 (bfs style), porblem is we dont know which side its on L4R5 here


#1,2,Null,Null,3,4,Null,Null,5,Null,Null
# left, right recursion 
#global pointer, with left and right recursion 
