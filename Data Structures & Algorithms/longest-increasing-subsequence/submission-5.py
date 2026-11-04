class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #brute force, at each index we choose to either skip it or take it if the value is greater than the previus value that we are looking at -> 2^n
        # if we can memorize the maxmimum length increasing subseuqeunce at each index, we could optimize this algrlthim actaully to never repeat the same state over and over again, boudning it by n, 2*n choices, whihch would become an O(N) algotrhitm time and space

     



        memo={}
        def dfs(index,value):

            if index==len(nums):
                return 0

            #if index in memo:
                #return memo[index] #each position in index represtsns the longest increasing seqeunce from that point 
            if (index,value) in memo:
                return memo[(index,value)]

            max_path=0

            if nums[index]>value:
                #we can take it 
                max_path=max(max_path,1+dfs(index+1,nums[index]))

            max_path=max(max_path,dfs(index+1,value))
            #print(f"we are currently looking at index:{index} prev value: {value}")
            #print(f"max path: {max_path}")
            #2 decisions take or not take
           #memo[index]=max_path
            memo[(index,value)]=max_path
            return memo[(index,value)]

        return dfs(0,-float('inf'))

        #brute force time: 2^n soluion Space: O(N) recursion stack  (either take it if its greater or do not take it)-> take maximum 
        
        #simple optpimization we can meorize the longest path for each previous state




        