# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #ccrate string in preorder n inroder
        #contacts pre + / + in
        def pot(roo):
            if not roo:
                return '#'
            l=pot(roo.left)
            r=pot(roo.right)
            return f"{roo.val},{l},{r}" # should return accureately
        return pot(root)

        

    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        da=data.split(",")# splits into array each coponent seperated by ,
        ind=0
        print(da)
        def sol():
            nonlocal da
            nonlocal ind
            if ind>=len(da):
                return None
            if da[ind]=='#':
                ind+=1
                return None
            roo=TreeNode(da[ind])
            ind+=1
            roo.left=sol()#the thought is that the it will keep hitting left n updating the left 
            roo.right=sol()#after done w right the ind will bupdated and will play w the 
            return roo
        return sol()
            
        
