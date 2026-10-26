class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        to enforce non duplcaites we either choose one index any can be chosen, as long as equal or above 
        we can memorize the state
        """



        #you can do this with dp, bascilly for each coin amount you store an array (O(N)) and will create a new array referecning it and then from there you replace it and continue till you reach teh end 

        #the idea here is that for each coin we consdier if its reachable (base case), also consider preious pd state add to it to get all reachabel states up to that mount 
        dp=[0]*(amount+1)
        dp[0]=1

        
        for coin in coins:
            for index in range(coin,amount+1):
                dp[index]+=dp[index-coin] #instead of two just updat e
            #then flip    
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

