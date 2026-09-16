class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lR,rR=0,len(matrix)-1
        lC,rC=0,len(matrix[0])-1

        #figuring out the row is log(row)
        #binary on the rows to figure out the row
        def findRow(lR,rR):
            while lR<=rR:
                midR=lR+(rR-lR)//2
                if matrix[midR][0]<=target<=matrix[midR][-1]:
                    return midR
                elif matrix[midR][0]<target:
                    lR=midR+1
                elif  matrix[midR][0]>target:
                    rR=midR-1
            return -1
        
        row=findRow(lR,rR)
        if row==-1:
            return False

        while lC<=rC:
            mid=lC+(rC-lC)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                rC=mid-1
            else:
                lC=mid+1
        return False
        
