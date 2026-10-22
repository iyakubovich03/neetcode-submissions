class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # brute force try every different combinatoin and check whether it equals teh target, O(n^2)
        # is there a way to do this in O(N)        


        """
        -slighlty more optimila ppaorch, sort the triplets three tims based on teh first index, second index, and third index, then run a binary serach to find the equal value or less than value at each point, logn, then take subarray, turn to set, and take intersection, roughly this algo is NLogn *3, then logn * 3, then O(N+M), so its NLogN, then sapce wise N 
        """
        if len(triplets)==1:
            return target==triplets[0]
        
        """
        def binary_search(value,index):
            #we are finding the last index that occurs for this vlaue 
            last_occurence=None
            l,r=0,len(triplets)-1
            while l<=r:
                mid=l+(r-l)//2
                if triplets[mid][index]>value:
                    r=mid-1
                elif triplets[mid][index]<value:
                    l=mid+1
                else:
                    last_occurence=mid
                    l=mid+1
            return last_occurence# if None means never occured 
        
        #bascilly we itearte over every value 
        for index in range(len(target)):
            #start with the first value
            triplets.sort(key=lambda x:x[index])
            partition_index=binary_search(target[index],index)
            if partition_index is None: #impossible
                return False
            #otherwise we partiion it 
            triplets=triplets[:partition_index+1]

        return len(triplets)>=2

        #O(N) approach 
        #nlogn runtime O(n) space
        """
        current_set=set()
        for a,b,c in triplets:
            current_set.add((a,b,c))
        
        for index in range(len(target)):

            current_max_limit=target[index]
            #its okay to have less than but must be at least one equal value 
            seen=False
            for candidate in current_set.copy():#O(N)*3
                if candidate[index]>current_max_limit:
                    current_set.remove(candidate)
                elif candidate[index]==current_max_limit:
                    seen=True

            if not seen: 
                return seen
                
        return len(current_set)>=2
    

        #[one_value,two_value,three_value]

       
