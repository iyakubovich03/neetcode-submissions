from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colT=defaultdict(set)
        rowT=defaultdict(set)
        square=defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[0])):
                value=board[row][col]
                if value==".":
                    continue
                if value in colT[col] or value in rowT[row] or value in square[(row//3,col//3)]:
                    return False
                colT[col].add(value)
                rowT[row].add(value)
                square[(row//3,col//3)].add(value)

        return True
        