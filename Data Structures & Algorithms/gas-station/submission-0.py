class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        brute force: iterate over every starting index of gas, then check if currentTotal gas >cost contineu and if you reach the sam index again, then we know it can be reached and we immeditlay return 
        O(N^2) space: O(1)

        O(N) time 
        

        gas:  1,2,3,4.     (looking for greatest position doesnt work ) -4,-3,-2,1
        cost: 5,1,2,1

        #want to know if we can stay 0>= throughout , and we know one location has that 

        [-4,-3,-2,3] #we know theres only one solution possible (meaing if it exists then thats where the maxSum would be and the minValue would be) 

        #if difference equals=0 its possible 
        -1,0,-2,1 (spo where we become positive is the possible)
        -1,-2,-1

        #second idea track the differnce between gas cost sum over both arrays, when it beceoms positive thta index is valid 

        #[-1,0,-1,3] (difference ), at each point we need to know if we have enough to reach the same index (looking at the sum, first time we hit positive, 
        
        

        #[-1,-1,1]

        #[-4,1,1,3] #at a certain index do we have a big enough sum to overgo the negatives, but position matter



        #[-4,1,-2,5]

        #[-4,1,-2,5]

        #prefix array and then rolling sum 
        """
        gas_sum=sum(gas)
        cost_sum=sum(cost)
        if gas_sum<cost_sum:
            return -1
        pointer=0
        total=0
        for index in range(len(gas)):
            total+=gas[index]-cost[index]
            if total<0:
                pointer=index+1
                total=0
        return pointer
        
        