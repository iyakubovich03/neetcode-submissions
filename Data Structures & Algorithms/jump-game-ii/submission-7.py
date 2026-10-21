class Solution:
    def jump(self, nums: List[int]) -> int:

        """
        dp[i]= the minimum number of jumps to reach len(nums)-1
        traverse from the end and we look at each possible jump that can be made, update with the minimum value
        -1 represetns unreachable state, and , conitue 
        space: O(N) 
        time: O(N*A_i)


        """

        """
        dp=[-1]*len(nums) #minimum number of steps requried to reach the end 
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
        """
        #if len(nums)==1:
        #   return 0
        
        jumps=0
        start=0
        end=0
        #now we do a level order traversal till we reach the end 
        while end<len(nums)-1:
            jumps+=1
            temp=end+1
            for index in range(start,end+1):
                end=max(end,index+nums[index])
            start=temp

        return jumps
        
        """
        minimum jumps using dp, tehcncially a dfs algo, could also use bfs (first time you hit a cell thats the min jump, do this till you reach end (but by doing this you tierate over every possible neighbor, then put it on the heap, need a visited set, and contously do this O(N^2)), instead of itreating over every neighbor, create a border for the level, start,end then from there grab the max border and update the start, once you find last cell retrun )


        """

        