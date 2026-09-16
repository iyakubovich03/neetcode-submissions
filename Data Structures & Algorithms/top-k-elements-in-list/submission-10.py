from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap=defaultdict(int) #O(N)
        for num in nums:
            frequencyMap[num]+=1
        frequencyBucket=[[] for _ in range(len(nums)+1)] 
        for key,value in frequencyMap.items(): #O(N)
            frequencyBucket[value].append(key)
        result=[]
        for index in range(len(frequencyBucket)-1,-1,-1):
            for element in frequencyBucket[index]:
                result.append(element)
                if len(result)==k:
                    return result
        return result
        #time O(N) space (O(N))
        