from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(row,col):
            if row<0 or row>=len(board) or col<0 or col>=len(board[0]) or board[row][col]!="O" or (row,col) in visited:
                return
            visited.add((row,col))
            
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
            #should traverse the whole point 
    
        not_surrounded=set()
        for col in range(len(board[0])):
            if board[0][col]=="O":
                not_surrounded.add((0,col))
            if board[len(board)-1][col]=="O":
                not_surrounded.add((len(board)-1,col))
        for row in range(len(board)):
            if board[row][0]=="O":
                not_surrounded.add((row,0))
            if board[row][len(board[0])-1]=="O":
                not_surrounded.add((row,len(board[0])-1))
        #have your non surrounded set:
        visited=set()
        for row,col in not_surrounded:
            if (row,col) not in visited:
                dfs(row,col)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]=="O":
                    board[row][col]="X"
        for row,col in visited:
            board[row][col]="O"


    

        #run dfs from each point 