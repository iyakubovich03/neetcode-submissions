class Solution:
    def jump(self, nums: List[int]) -> int:

        """
        dp[i]= the minimum number of jumps to reach len(nums)-1
        traverse from the end and we look at each possible jump that can be made, update with the minimum value
        -1 represetns unreachable state, and , conitue 
        space: O(N) 
        time: O(N*A_i)


        """
        dp=[-1]*len(nums)
        dp[-1]=0

        for index in range(len(nums)-2,-1,-1): #O(N)
            current_jump_max=nums[index]+1

            minimum_jump=float('inf')
            for jump in range(1,current_jump_max): #O(A)
                new_index=index+jump
                
                if new_index>=len(nums):
                    break
                elif dp[new_index]==-1:
                    continue

                minimum_jump=min(minimum_jump,dp[new_index])
            if minimum_jump==float('inf'):
                continue

            dp[index]=minimum_jump+1

        return dp[0]
                

        