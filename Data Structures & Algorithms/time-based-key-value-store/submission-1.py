from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timeMap=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #we do a 
        self.timeMap[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        #binary search on time 
        if not self.timeMap[key]:
            return ""

        l,r=0,len(self.timeMap[key])-1
        value=""
        while l<=r:
            mid=l+(r-l)//2
            # we can grab the closest Timestamp, but we want to bring the value 
            currentTime,currentValue=self.timeMap[key][mid]
            if currentTime==timestamp:
                return currentValue
            elif currentTime<timestamp:
                value=currentValue
                l=mid+1
            else:
                r=mid-1
        return value

        
