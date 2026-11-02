class Solution:
    def hammingWeight(self, n: int) -> int:


        #23.               168421.   10111 number 
        # convert n into a bit then into a string and count the 1s  O(N) O(N)
        # each 1 bit represents a value of 2
        # you can also inalize a counter for expoennet and bascilly and xor the value
        # brute force, bascilly enter while loop expoenitating to find closest value biggest thats smalelst, incrment then subtract then repeat 


        # bascilly what we want to do is if the value is 1 we want to xor it 
        start=0
        count=0
        
        while 2**start<=n:
            if (((2**start) ^ n) & 2**start) == 0: # 1000.  11000
                count+=1
            start+=1
        return count



        