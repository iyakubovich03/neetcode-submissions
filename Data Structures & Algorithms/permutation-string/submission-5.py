class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1Frequency=[0]*26
        s2Frequency=[0]*26

        for value in s1:
            s1Frequency[ord(value)-ord('a')]+=1
       
        l=0
        for r,value in enumerate(s2):
            currentValue=s2[r]
            s2Frequency[ord(currentValue)-ord('a')]+=1

            while r-l+1>len(s1):
                lValue=s2[l]
                s2Frequency[ord(lValue)-ord('a')]-=1
                l+=1

            if s1Frequency==s2Frequency:
                return True
   
        return False

        