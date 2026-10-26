class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack=[] #start before or equal last values end time that means they overlap, meanig we can pop off and merge
        for start,end in intervals:

            if stack and stack[-1][1]>=start:
                #we pop 
                prev_start,prev_end=stack.pop()
                stack.append([prev_start,max(end,prev_end)])
            else:
                stack.append([start,end])
        return stack