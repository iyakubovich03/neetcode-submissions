import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        #idea is that we only need k sub interval size 
        heapq.heapify(self.nums)
        while len(self.nums)>self.k:
            heapq.heappop(self.nums)#want the 3 biggest value drop all teh values until legnht is 3
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)#this needs to be heapieid?
        while len(self.nums)>self.k:
             heapq.heappop(self.nums)
        return self.nums[0]

       