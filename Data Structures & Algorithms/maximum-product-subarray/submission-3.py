class Solution:
    def maxProduct(self, nums: List[int]) -> int:

       #track current sum, also track smallest value, when hit 0 take max w 0, but reset the current to 1, and the min 
        maxGlobal=-float('inf')
        current=1
        smallest=1

        for n in nums:
            if n==0: #reset
                maxGlobal=max(maxGlobal,0)
                current=1
                smallest=1
                continue

            current*=n
            if current>0:
                maxGlobal=max(maxGlobal,current)
            else:
                maxGlobal=max(maxGlobal,int(current//smallest))

            if n<0 and n<smallest:
                smallest=current

        return maxGlobal

            
        



        

