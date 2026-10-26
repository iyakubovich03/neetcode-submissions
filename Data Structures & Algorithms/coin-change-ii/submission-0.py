class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        to enforce non duplcaites we either choose one index any can be chosen, as long as equal or above 
        we can memorize the state
        """

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


