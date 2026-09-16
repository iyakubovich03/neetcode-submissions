class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1Frequency=[0]*26
        for value in s1:
            s1Frequency[ord(value)-ord('a')]+=1
        s2Frequency=[0]*26
        pointsNeeded=sum(1 for s in s1Frequency if s!=0)
        l,r=0,0
        currentPoints=0
        while r<len(s2):
            currentValue=s2[r]
            s2Frequency[ord(currentValue)-ord('a')]+=1
            if s2Frequency[ord(currentValue)-ord('a')]==s1Frequency[ord(currentValue)-ord('a')]:
                currentPoints+=1
            while r-l+1>len(s1):
                lValue=s2[l]
                s2Frequency[ord(lValue)-ord('a')]-=1
                if s1Frequency[ord(lValue)-ord('a')]-1==s2Frequency[ord(lValue)-ord('a')]:
                    currentPoints-=1
                l+=1
            if currentPoints==pointsNeeded:
                return True
            r+=1
        return False

        