class Solution:
    def climbStairs(self, n: int) -> int:
        #visited=set()#track 
        count=0 #tracks possibiltiies 
        #there are alot of cases where repeatd elemnts will occur 
        #track repeated paths 
        visited_value={}

        #how do i properly track viisted sets 
        def count_number(value):
            nonlocal visited_value
            nonlocal n

            if value in visited_value:#means its valid only want visited to be added if its valid 
                return visited_value[value]
            if value == n: #means you got to the conditon   
                return 1
            if value>n:#we want to discard this pathway 
                return 0

            val1=count_number(value+1)
            #ex: goes all the way down we track this valid 
            val2=count_number(value+2)
            #only add visited if it reaches true
            visited_value[value]=val1+val2
            return val1+val2#pass this value up 
     
        return count_number(0)

            #assume we track 
            #if it gets to 0 we will add that value 
            # we start from 0 n compute 
        