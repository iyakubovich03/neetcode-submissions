class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #fire we look for the proper interval 
        def recSearchMatrix(lowerRowBound,upperRowBound,lowerColBound,upperColBound,arr,target):
            midRow=lowerRowBound+(upperRowBound-lowerRowBound)//2

            if lowerRowBound>upperRowBound:
                return False #this is hte case where no row has the answer immeditaly foudn in Log n 
            if arr[midRow][0]<=target<=arr[midRow][len(arr[0])-1]:
                midCol=lowerColBound+(upperColBound-lowerColBound)//2
                if lowerColBound>upperColBound:
                    return False
                if arr[midRow][midCol]==target:
                    return True
                if arr[midRow][midCol]>target:
                    #recurse left
                    return recSearchMatrix(lowerRowBound,upperRowBound,lowerColBound,midCol-1,arr,target)
                else:
                    return recSearchMatrix(lowerRowBound,upperRowBound,midCol+1,upperColBound,arr,target)
                #now its just white n black binary 
                #then we recruse inside 
            elif target<arr[midRow][0]:
                return recSearchMatrix(lowerRowBound,midRow-1,lowerColBound,upperColBound,arr,target)# this recruses the row 

            elif target>arr[midRow][len(arr[0])-1]: #accounts for case where target 
                return recSearchMatrix(midRow+1,upperRowBound,lowerColBound,upperColBound,arr,target)

        if not matrix:
            return False   
        return recSearchMatrix(0,len(matrix)-1,0,len(matrix[0])-1,matrix,target)