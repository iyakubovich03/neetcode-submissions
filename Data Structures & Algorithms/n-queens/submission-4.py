class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:


        result=[]
        current=[["."]*n for _ in range(n)]
        column=set()
        leftToRight=set()
        rightToLeft=set()

        def recursive(row):
            if row==n: 
                result.append(["".join(r) for r in current])
                return 

            for col in range(n):
                if col in column or row-col in leftToRight or row+col in rightToLeft:
                    continue
       
                column.add(col)
                leftToRight.add(row-col)
                rightToLeft.add(col+row)
                current[row][col]="Q"

                recursive(row+1)

                current[row][col]="."
                column.remove(col)
                leftToRight.remove(row-col)
                rightToLeft.remove(col+row)
            

   
        recursive(0)
        return result 
