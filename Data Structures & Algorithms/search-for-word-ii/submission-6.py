class trieNode():
    def __init__(self):
        self.nextCharacter={}
        self.word=""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        parentNode=trieNode()
        
        for word in words:
            reference=parentNode
            for w in word:
                if w not in reference.nextCharacter:
                    reference.nextCharacter[w]=trieNode()
                reference=reference.nextCharacter[w]
            reference.word=word
            
        #created this trie data structure 
        result=[]
        direction=[[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(currentNode,row,col):
            currentParent=currentNode.nextCharacter[board[row][col]]
            #print(f"current value: {board[row][col]}")
            #print(f"currentNode vlaue {currentNode.word}")
            if currentParent.word:
                result.append(currentParent.word)
                currentParent.word=""
                if not currentParent.nextCharacter:
                    del currentNode.nextCharacter[board[row][col]]
                    return
#temporary way of not adding (there is a way to prune)

            currentValue=board[row][col]
            board[row][col]="#"
            for dr,dc in direction:
                nr,nc=row+dr,dc+col
                if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] in currentParent.nextCharacter:
                    
                    dfs(currentParent,nr,nc)
                    #more pruning here 
            if not currentParent.word and not currentParent.nextCharacter:
                del currentNode.nextCharacter[currentValue]

            board[row][col]=currentValue

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in parentNode.nextCharacter:
                    dfs(parentNode,row,col)

        return result
            
        #we still explore words for no reason 

        