class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # after you sell neetCoin i-th day, you cannot buy one on the i+1 th day 
        # you must buy then sell, you cannot buy,buy then sell sell, so after a buy operation you must sell
        # need a way to distinguish buying and selling 
        # brute: try every possible combination, 1st: buy or skip (if we have current balance then we can buy, then add to current total, and reset to selling) #there is no point of ever going negative (not optimal so if that is the case we can just break off )

        memo={}

        def dfs(index,current_buying,state,current_profit):

            if index>=len(prices):
                return current_profit

            if (index,current_buying,state,current_profit) in memo:
                return memo[(index,current_buying,state,current_profit)]

            max_value=0

            if state=="selling" and current_buying<=prices[index]: #only sell when goes positive 
                max_value=max(max_value,dfs(index+2,0,"looking",current_profit+(prices[index]-current_buying)))

            max_value=max(max_value,dfs(index+1,current_buying,state,current_profit))

            if state=="looking": #meaning we can buy 
                max_value=max(max_value, dfs(index+1,prices[index],"selling",current_profit))

            memo[(index,current_buying,state,current_profit)]=max_value

            return memo[(index,current_buying,state,current_profit)]

        return dfs(0,0,"looking",0)

        """
        memo={}

        def dfs(index,current_buying,current_profit):

            if index>=len(prices):
                return current_profit

            if (index,current_buying,currrent_profit) in memo:
                return memo[(index,current_buying,currrent_profit)]

            #we can either buy (if balance is 0), or do nothing skip, or  if stock then sell and update profit, and lanace to 0 
            max_value=0
            if current_buying and current_buying<prices[index]: #only sell when goes positive 
                max_value=max(max_value,dfs(index+1,0,current_profit+(prices[index]+current_buying)))

            #do nothing 
            max_value=max(max_value,dfs(index+1,current_buying,current_profit))

            #or we can buy 
            if current_buying==0: #meaning we can buy 
                max_value=max(max_value, dfs(index+1,prices[index],current_profit))

            meom[(index,current_buying,currrent_profit)]=max_value
            return (index,current_buying,currrent_profit)]

       return dfs(0,0,0)

       # 2 desciison at each point  2^N runtmie 
       # maximum possible states (index can go to N), i think tis something like 3^N , we are uisng memo 
        
        """
       
