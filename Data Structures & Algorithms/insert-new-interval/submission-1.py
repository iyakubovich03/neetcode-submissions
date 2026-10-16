class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        find the posiiton where to add the enw intereral (while end<start)
        then decide either to merge directly or just add sepetaely 

        pointer=0
        while end<start:
            pointer+=1
        #check if oldStart<start: then merge otherwise just apepnd 
        #we continue potetilly merging from there with a stack logic, checking if start<end then pop and merge

        """

        pointer=0
        result=[]
        while pointer<len(intervals) and intervals[pointer][1]<newInterval[0]:
            result.append(intervals[pointer])
            pointer+=1
        #potentially we are the end 
        if pointer==len(intervals):
            result.append(newInterval)
            return result
        
        #otherise we check if merge needed 
        if newInterval[0]>=intervals[pointer][0]:
            result.append([intervals[pointer][0],max(intervals[pointer][1],newInterval[1])])
            pointer+=1
        else:
            result.append(newInterval)

        for index in range(pointer,len(intervals)):
            start,end=intervals[index]
            if result and result[-1][1]>=start:
                prevStart,prevEnd=result.pop()
                result.append([min(prevStart,start),max(prevEnd,end)])
            else:
                result.append([start,end])

        return result




        

        