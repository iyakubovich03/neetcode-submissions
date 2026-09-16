class Solution:
    def climbStairs(self, n: int) -> int:
        #visited=set()#track 
        count=0 #tracks possibiltiies 
        def count_number(value):
            nonlocal count
            #if it gets to 0 we will add that value 
            if value==0:
                count+=1
                return 
            if value<0 :
                return 
           # if value-1 not in visited:
            #visited.add(value-1)
            val1=count_number(value-1)
                
            #if value-2 not in visited:
            #visited.add(value-2)
            val2=count_number(value-2)
            
            
            #at the base case 
            #it will recurse otwards
        count_number(n)
        return count
                
        