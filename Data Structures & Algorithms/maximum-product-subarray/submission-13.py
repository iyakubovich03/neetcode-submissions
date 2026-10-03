class Solution:
    def maxProduct(self, nums: List[int]) -> int:

       #track current sum, also track smallest value, when hit 0 take max w 0, but reset the current to 1, and the min 
        maxGlobal=-float('inf')
        current=1
        smallest=None

        for n in nums:

            if n==0: #reset
                maxGlobal=max(maxGlobal,0)
                current=1
                smallest=None
                continue

            current*=n
            

            if current<0 and smallest:
                 maxGlobal=max(maxGlobal,int(current/smallest))
            maxGlobal=max(maxGlobal,current)
            
            if current<0 and (smallest is None or current>smallest):
                smallest=current
            #print(f"smallest val: {smallest}")
        return maxGlobal

        #O(N) O(1)
            
        



        

