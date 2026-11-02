class Solution:
    def maxCoins(self, nums: List[int]) -> int:
       #think of htis problem form the back. Chose the elemnt you are going to pop last recursively 

        memo={} # for (l,r)= max value possible 

        modified_array=[1]+nums+[1]

        def dfs(l,r):
            #we bascilly do it until we cannot 
            left_side=modified_array[l-1]
            right_side=modified_array[r+1]
            #then we iterate and choose the elemtn 
            if (l,r) in memo:
                return memo[(l,r)]
            max_coins=0
            for index in range(l,r+1):
                #choose this element 
     
                max_coins=max(max_coins,modified_array[index]*left_side*right_side+dfs(l,index-1)+dfs(index+1,r))
            
            memo[(l,r)]=max_coins
            return  memo[(l,r)]

        return dfs(1,len(modified_array)-2)
            


