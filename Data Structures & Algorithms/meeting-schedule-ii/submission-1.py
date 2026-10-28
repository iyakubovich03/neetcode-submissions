
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #we want to put the intervals in incerasing order of start time, when an overlap occurs a new room is needede, however if the earlies end is afer the enw start we can simply replace it with tthe same room, we can do this for all the itnervals and return the list of teh heap 
        heap=[]
        intervals.sort(key=lambda Interval: Interval.start)
        for interval in intervals:
            start,end=interval.start,interval.end
            if heap and heap[0]<=start:
                heapq.heappop(heap)
                heapq.heappush(heap,end)
            else:
                heapq.heappush(heap,end)

        return len(heap)

        