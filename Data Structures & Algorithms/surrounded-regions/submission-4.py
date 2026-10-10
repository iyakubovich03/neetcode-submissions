class Solution:
    def solve(self, board: List[List[str]]) -> None:
        notSurrounded=set()
        #iterate over edges n run dfs 
        #iterate over grid and if equal to O and not in set then set to X
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(row,col):
            notSurrounded.add((row,col))
            for dr,dc in directions:
                nr=row+dr
                nc=col+dc
                if (nr,nc) not in notSurrounded and 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc]=="O":
                    dfs(nr,nc)

        for col in range(len(board[0])):
            if (0,col) not in notSurrounded and board[0][col]=="O":
                dfs(0,col)
            if (len(board)-1,col) not in notSurrounded and board[len(board)-1][col]=="O":
                dfs(len(board)-1,col)
        
        for row in range(len(board)):
            if (row,0) not in notSurrounded and board[row][0]=="O":
                dfs(row,0)
            if (row,len(board[0])-1) not in notSurrounded and board[row][len(board[0])-1]=="O":
                dfs(row,len(board[0])-1)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row,col) not in notSurrounded and board[row][col]=="O":
                    board[row][col]="X"
        


        