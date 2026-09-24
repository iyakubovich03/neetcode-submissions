class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        direction=[[-1,0],[0,-1],[0,1],[1,0]]

        def dfs(row,col,index):
            if index==len(word):
                return True

            currentValue=board[row][col]
            board[row][col]="#"

            for dr,dc in direction:
                nr=row+dr
                nc=col+dc
                if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc]==word[index]:
                    if dfs(nr,nc,index+1):
                        return True

            board[row][col]=currentValue
            return False


        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]==word[0] and dfs(row,col,1) :
                    return True
        return False
                    
            
        