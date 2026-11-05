class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #brute force, at each index we choose to either skip it or take it if the value is greater than the previus value that we are looking at -> 2^n
        # if we can memorize the maxmimum length increasing subseuqeunce at each index, we could optimize this algrlthim actaully to never repeat the same state over and over again, boudning it by n, 2*n choices, whihch would become an O(N) algotrhitm time and space

        #other 
        #the idea is we would iterate over every value, base is length 1

        #space optimizaiotn, bascilly each state will rerepsent the maximum increasing length (inclusive)

        result=[]

        def binary_search(left,right,target):

            while left<right:

                mid=left+(right-left)//2\

                if result[mid]>=target:
                    right=mid
                else:
                    left=mid+1

            return left #have foudn the first index

        for num in nums:
            next_index=binary_search(0,len(result),num)
            if next_index==len(result):
                result.append(num)
            else:
                #we replcae 
                result[next_index]=num
        return len(result)


        
            


        """
        #dp solution one array 
        dp=[1]*len(nums)
        max_seen=1

        for index in range(len(nums)):
            current_value=nums[index]
            for next_index in range(index+1,len(nums)):
                next_value=nums[next_index]
                if current_value<next_value:
                    dp[next_index]=max(dp[next_index],dp[index]+1)
                    max_seen=max(max_seen,dp[next_index])

        return max_seen
        #clean O(n^2) time case, and O(N) space 
                
        """

        """
        memo={}
        def dfs(index):
            if index in memo: #represents the longest paths 
                return memo[index]# this is the maxmimum possible length from this cell 

            current_number=nums[index]
            max_length=1
            for next_index in range(index+1,len(nums)):
                #we cehkc greater and recruse 
                next_number=nums[next_index]

                if current_number<next_number:
                    max_length=max(max_length,1+dfs(next_index))

            memo[index]=max_length
            return memo[index]

        max_value=1
        for index in range(len(nums)):
            max_value=max(max_value,dfs(index))
        return max_value 
        """
        #optiomized bascilly each state represents the longest subsequence for that index 

        #we memorize N states, and we iterate over each state but each is memorized, runtime is O(n^2)




        """
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
        #at each index we mermozie the longest possible seqeunce with particular preivous state
        #each index for n-1 values so roughly its n^2 cases, time n space its n^2 (by memorizing each state and previous value)
        """



        