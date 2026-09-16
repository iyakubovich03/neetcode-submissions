class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        count=[0]*26
        tcount=[0]*26
        matches=0
        l=0
        for i in range(len(s1)):
            index1=ord(s1[i])-ord('a')
            count[index1]+=1
            index2=ord(s2[i])-ord('a')
            tcount[index2]+=1
        for i in range(26):
            if count[i]==tcount[i]:
                matches+=1
        for j in range(len(s1),len(s2)):
            if matches==26:
                return True
            index=ord(s2[j])-ord('a')
            tcount[index]+=1
            if tcount[index]==count[index]: #this checking when you add it is good
                matches+=1
            elif tcount[index]==count[index]+1:
                matches-=1

            index=ord(s2[l])-ord('a')
            tcount[index]-=1
            if tcount[index]==count[index]-1: #two cases left going right its on a continous basis to see if its a permutation so it will know 
                matches-=1
            elif tcount[index]==count[index]:
                matches+=1
            l+=1
        return matches==26
            
            
            

