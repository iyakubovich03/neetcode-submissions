class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h=set()
        l=0
        track=0
        for i in range(len(s)):
            while s[i] in h:
                h.remove(s[l])
                l+=1
            h.add(s[i])
            track=max(track,i-l+1)   
        return track          

            

