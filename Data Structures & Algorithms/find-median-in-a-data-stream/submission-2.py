import heapq
class MedianFinder:

    def __init__(self):
        self.smallerValues=[] #max heap
        self.biggerValues=[] #min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallerValues,-num)

        if len(self.smallerValues)-len(self.biggerValues)>1:
            #then we pop and append 
            leftSideValue=heapq.heappop(self.smallerValues)   
            heapq.heappush(self.biggerValues,-leftSideValue)
        #now we check if imbalance

        if self.biggerValues and -(self.smallerValues[0])>self.biggerValues[0]:
            swap1,swap2=-heapq.heappop(self.smallerValues),-heapq.heappop(self.biggerValues)
            heapq.heappush(self.smallerValues,swap2)
            heapq.heappush(self.biggerValues,swap1)

    def findMedian(self) -> float:
        if (len(self.smallerValues)+len(self.biggerValues))%2==0:
            return (-self.smallerValues[0]+self.biggerValues[0])/2

        return -self.smallerValues[0]
        
        