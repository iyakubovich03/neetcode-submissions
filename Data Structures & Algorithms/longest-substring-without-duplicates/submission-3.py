class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res=0
        p=set()
        for i in range(len(s)):
            while s[i] in p:
                p.remove(s[l])
                l+=1
            p.add(s[i])
            res=max(res,i-l+1)
        return res
            