from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        globalMax=0
        frequencyMap=defaultdict(int)
        l=0
        maxSeen=0
        for index,value in enumerate(s):
            frequencyMap[value]+=1
            maxSeen=max(maxSeen,frequencyMap[value])
            while ((index-l+1)-maxSeen)>k:
                frequencyMap[s[l]]-=1
                l+=1
            globalMax=max(globalMax,index-l+1)
        return globalMax
            

                

        