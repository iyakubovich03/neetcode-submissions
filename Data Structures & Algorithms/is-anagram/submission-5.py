class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):
            return False
        to={}
        l={}
        for i in s:
            to[i]=to.get(i,0)+1
        for j in t:
            l[j]=l.get(j,0)+1
        return to==l
    
        