class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        one_step_back=cost[1]
        two_step_back=cost[0]

        for index in range(2,len(cost)):
            smallerValue=min(one_step_back,two_step_back)
            currentValue=cost[index] if 0<=index<len(cost) else 0
            one_step_back,two_step_back=smallerValue+currentValue,one_step_back

        return min(one_step_back,two_step_back)        #O(N)