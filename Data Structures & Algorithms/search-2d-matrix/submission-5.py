class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)*len(matrix[0])-1
        row,col=len(matrix),len(matrix[0])
        #same idea as before just convert the values instead of binary over rows
        while l<=r:
            mid=l+(r-l)//2
            currentRow=mid//col
            currentCol=mid%col
            if matrix[currentRow][currentCol]==target:
                return True
            elif matrix[currentRow][currentCol]>target:
                r=mid-1
            else:
                l=mid+1
        return False
            
        
