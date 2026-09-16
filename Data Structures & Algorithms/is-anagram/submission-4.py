class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        one = {}
        two={}
        for l in s:
            if l in one:
                one[l]+=1
            else:
                one[l]=1
        for i in t:
            if i in two:
                two[i]+=1
            else:
                two[i]=1

        if one!=two:
            return False
        return True