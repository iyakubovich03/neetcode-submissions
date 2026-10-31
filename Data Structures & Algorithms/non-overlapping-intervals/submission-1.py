class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # the minimum number of intervals to remove such that , the rest of the intervals are not overlapping
        # you can reduce the minimum of overlapping intervals by greedily chosoing the ones that intersect with the most intervals, (1,4): overlaps 2 intervals,  check 1<=start<4
        #brute force would be to track the interval that overlaps the most, and remove it, then reclaluate and remove stop when no overlapping intervals exist 

        #O(N^2)*roughly N times O(N^3)


        # [1,3],[1,4],[0,2]. -> remove 2
        

        # 1,4 1,2 2,3 (j iterating you would asssume its 2) however the max is 0,4 , remove that and no more 
        #ONCE YOU know the max, you remove it how do you know the next max, 

        # we check 1<= el < 4  2 overlap 
        # remove that one, then update 


        # 1,2.  1,4. 2,4.       overlaps turns to ([1,2, 1,4,2,4])


        intervals.sort(key=lambda interval:interval[1])
        min_to_remove=0
        s,e=intervals[0]
        for index in range(1,len(intervals)):
            new_start,new_end=intervals[index]
            if new_start<e:
                min_to_remove+=1
            else:
                s,e=new_start,new_end
                
        return min_to_remove

        