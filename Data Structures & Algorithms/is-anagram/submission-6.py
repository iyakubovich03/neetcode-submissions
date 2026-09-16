class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        characterBucket=[0]*26
        for index in range(len(s)):
            sValue=s[index]
            tValue=t[index]
            characterBucket[ord(sValue)-ord('a')]+=1
            characterBucket[ord(tValue)-ord('a')]-=1
        for v in characterBucket:
            if v:
                return False
        return True #all characters have cancelled out #O(N) #O(1)
        

        