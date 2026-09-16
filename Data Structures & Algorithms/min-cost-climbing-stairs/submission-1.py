class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #you can move in two directions
        final_val=len(cost)#this is the max array 
        #how can i track the current hsortest path 
        min_dist={}
        #need a distance from the 
        def compute_shortest(index):
            #connect it n start at 0
            
            if index>=final_val:
                return 0 #the value
            if index in min_dist:
                return min_dist[index]
           # current store
        
            val1=compute_shortest(index+1)#adds current index (all of these will return a certain value)
            
            val2=compute_shortest(index+2)#adds current index 
            #all the way at the end 
            #it will iterate backwards 

            min_dist[index]=min(val1,val2)+cost[index]#the idea is that if it got back to this point it will be the smellest 
            return min(val1,val2)+cost[index]
        return min(compute_shortest(0),compute_shortest(1))
           #choosing the smallest edge doesnt necesarily lead to the smallest point 

        #the idea is that we traverse teh graph 
            
           #the runtime is shit #there are differnet approaches we want to preserve u