class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #dict w keys as 
        b=defaultdict(list)
        for i in strs:
            l=[0] *26
            for let in i:
                t=ord(let)-ord('a')
                l[t]+=1
                
            b[tuple(l)]+=[i]
        return b.values()

