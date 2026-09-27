class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr=[1]*(len(cost)+2)
        arr[0]=cost[0]
        arr[1]=cost[1]

        for index in range(2,len(arr)):
            smallerValue=min(arr[index-1],arr[index-2])
            currentValue=cost[index] if 0<=index<len(cost) else 0
            arr[index]=smallerValue+currentValue
            
        return min(arr[-1],arr[-2])
        