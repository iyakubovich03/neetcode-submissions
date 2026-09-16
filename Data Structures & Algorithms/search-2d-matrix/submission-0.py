class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        while (l<=r):
            middle=(l+r)//2
            if (matrix[middle][0]<=target and matrix[middle][len(matrix[middle])-1]>=target):
                l=0
                r=len(matrix[middle])-1
                while l<=r:
                    lo=(l+r)//2
                    if matrix[middle][lo]==target:
                        return True
                    if matrix[middle][lo]>target:
                        r=lo-1
                    elif matrix[middle][lo]<target:
                        l=lo+1
                return False
            elif(target>matrix[middle][len(matrix[middle])-1]):
                l=middle+1
            else:
                r=middle-1
        return False
        