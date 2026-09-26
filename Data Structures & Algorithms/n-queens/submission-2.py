class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:


        result=[]
        current=[] #which holds list of strings
        currentString=["."]*n

        column=set()
        leftToRight=set()
        rightToLeft=set()

        def recursive(row):

            if row==n: 
                result.append(current.copy())
                return 

        
            for col in range(n):
                if col in column or row-col in leftToRight or row+col in rightToLeft:
                    continue
       
                column.add(col)
                leftToRight.add(row-col)
                rightToLeft.add(col+row)

                currentString[col]="Q"
                current.append("".join(currentString))
                currentString[col]="."
                recursive(row+1)

                column.remove(col)
                leftToRight.remove(row-col)
                rightToLeft.remove(col+row)
                current.pop()
            #n^n * (n*n)
        recursive(0)
        return result 
