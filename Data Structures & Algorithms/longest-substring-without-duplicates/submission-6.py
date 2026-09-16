class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        val=0
        l=0
        r=0
        h=set()
        while l<=r and r<len(s):
            while s[r] in h:
                h.remove(s[l])
                l+=1
            val=max(val,r-l+1)
            h.add(s[r])
            r+=1
        return val
                

            

