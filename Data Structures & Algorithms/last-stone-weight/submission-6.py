import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr=[-s for s in stones]
        heapq.heapify(arr)
        while len(arr)>1:
            biggest_1=-(heapq.heappop(arr))
            biggest_2=-(heapq.heappop(arr))
            if biggest_1==biggest_2:
                continue #do nothing 
            else:
                heapq.heappush(arr,-(biggest_1-biggest_2))
        return -(arr[0]) if arr else 0


        