class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #dijstras only based on shortest path 
        #you can start from 0 or from 1 index
        #you can move +1 or +2 from every 
        #goal is to get to the an index above the last index
        #if you can jump over the last nidex you can idnex do this for free

        #if teh algo always chose the smalelst edge 
        #There are multiple paths you can take 
        #but you want to return teh shrotest one 
        #you have an array and you start iwth index
        final_val=len(cost)#this is the max array 
        def compute_shortest(index,val):
            #connect it n start at 0
            
            if index>=final_val:
                return val #the value
           # current store
        
            val1=compute_shortest(index+1,val+cost[index])#adds current index (all of these will return a certain value)
            
            val2=compute_shortest(index+2,val+cost[index])#adds current index 

            return min(val1,val2)
        return min(compute_shortest(0,0),compute_shortest(1,0))
           #choosing the smallest edge doesnt necesarily lead to the smallest point 
            
           #once it recheases bsae 
