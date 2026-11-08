# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# given a tree via root node and we want to convert/seralize it into a string , we can later deseraizlie/deconvert into the same structure 


# some method of traversing the tree structure and we can track the nodes we have seen as we iterate in an array and conver tit tinto a string at the end 
# based on the traversal, we can use the same traversal on the string later to recreate the same graph, when reaching null we can set it to "Null" value say we can use "*" 

#we iterate over the tree using a depth first serach and we track the nodes we have seen in a preorder traversal (when we see the node we mark it) adn then we reucrse left n to the right node 
#[] and join it into as tring and when we reach None, we can append "*"

#we would recruse in teh same exact way and we basiclly would create the node at the current index and then recurse left and then right connecting it, using a shared index, index+1 and iti will map to teh correct node that was recruse in teh same algo
#return the first node 

#time: O(Node+Edges) space: O(Nodes)
#O(Nodes+Edges) , auxilairy space its o(1) but if we ar econsdiering the output its would O(Node+edges)


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:

        result=[]

        def dfs(current_node):

            if not current_node:
                result.append("*")
                return 

            #we append the node we see in preorder 
            result.append(str(current_node.val))

            dfs(current_node.left)
            dfs(current_node.right)
        
        dfs(root)
        return "/".join(result)

        

        

    def deserialize(self, data: str) -> Optional[TreeNode]:

        data=data.split("/")
        shared_index=0

        def dfs():
            nonlocal shared_index
            
            #print(f"Shared index {shared_index}")

            if shared_index>=len(data) or data[shared_index]=="*":
                return None

            current_node=TreeNode(int(data[shared_index]))
            shared_index+=1
            current_node.left=dfs()
            shared_index+=1
            current_node.right=dfs()

            return current_node

        return dfs()

    # [1,2,*,*,3,4,*,*,5,*,*]

    # currentNode(1,) --> left (currentNode 2)--> * return None  right None
    #currentNode right 


    #inorder or in postorder (you can geenrate the same graph) 
    #you would need to find the root 
    #you would itearte over the root check if its the same value (node) duplaite node that looks the same \same vlaue same left node and same right node 
    #you have to find the node such that the trees are equiavelt 


        

            

