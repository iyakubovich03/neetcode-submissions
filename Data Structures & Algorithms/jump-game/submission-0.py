class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        we can iterate backwards
        mark a state reachable=len(nums)-1
        iterate backwards
        we basicilly check if curent index+jump>=reachable:
        update reachable 
        return reachabel=0
        O(N)
        O(1)
        """
        reachable_state=len(nums)-1
        
        for index in range(len(nums)-2,-1,-1):
            if index+nums[index]>=reachable_state:
                reachable_state=index
        return reachable_state==0
        

        