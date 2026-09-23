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
            #print(f"current value: {board[row][col]}")
            #print(f"currentNode vlaue {currentNode.word}")
            if currentNode.word:
                result.append(currentNode.word)
                currentNode.word="" #temporary way of not adding (there is a way to prune)

            currentValue=board[row][col]
            board[row][col]="#"
            for dr,dc in direction:
                nr,nc=row+dr,dc+col
                if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] in currentNode.nextCharacter:
                    
                    dfs(currentNode.nextCharacter[board[nr][nc]],nr,nc)
            board[row][col]=currentValue

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in parentNode.nextCharacter:
                    dfs(parentNode.nextCharacter[board[row][col]],row,col)

        return result
            

        