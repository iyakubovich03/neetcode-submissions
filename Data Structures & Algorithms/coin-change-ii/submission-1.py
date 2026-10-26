class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        to enforce non duplcaites we either choose one index any can be chosen, as long as equal or above 
        we can memorize the state
        """



        #you can do this with dp, bascilly for each coin amount you store an array (O(N)) and will create a new array referecning it and then from there you replace it and continue till you reach teh end 
        dp=[0]*(amount+1)
        dp[0]=1
        current_array=[0]*(amount+1)
        current_array[0]=1
        
        for coin in coins:
            #itearte over all of the values 
            for index in range(1,amount+1):
                if index-coin>=0:
                    current_array[index]+=current_array[index-coin]
                current_array[index]+=dp[index]
        
            #then flip 
            dp=current_array
            current_array=[0]*(amount+1)
            current_array[0]=1
        
        return dp[-1]
                
                    

        """
        # bascilly choose the coin or next (but once you choose next you cannot choose the next) (avoids duplicates)
        # we can memroize the current (index,amount) the state (number of unique ways to reach that path), 
        # Runtime O(N*M)
        # space(N*M)


        memo={}

        def dfs(index,current_amount):

            if current_amount==amount:
                return 1 
            
            if current_amount>amount:
                return 0

            if (index,current_amount) in memo:
                return memo[(index,current_amount)]

            unique_paths=0
            for current_index in range(index,len(coins)):
                unique_paths+=dfs(current_index,current_amount+coins[current_index])

            memo[(index,current_amount)]=unique_paths

            return memo[(index,current_amount)]

        return dfs(0,0)
        """

