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
        #look for elemnts with first elment case, then make sure it doesnrt get eliminated from teh other indexes, meaning it hosuld euqal or be less than ad smae with 3
        #we don need as et
        rolling_x,rolling_y,rolling_z=1,1,1
        for a,b,c in triplets:
            if a>target[0] or b>target[1] or c>target[2]:
                continue

            rolling_x=max(rolling_x,a)
            rolling_y=max(rolling_y,b)
            rolling_z=max(rolling_z,c)
        print()
        return [rolling_x,rolling_y,rolling_z]==target
            
        #O(N)
        #hypotheticlaly we can do this shirnking but we must make sure we ill have candidates for teh last two vlaues (based on like freuqncey )

        #[one_value,two_value,three_value]

       
