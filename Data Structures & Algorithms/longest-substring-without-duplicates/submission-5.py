class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        val=0
        po=set()
        for i in range(len(s)):
            while s[i] in po:
                po.remove(s[l])
                l+=1
            po.add(s[i])
            val=max(i-l+1,val)
        return val
