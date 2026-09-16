class Solution:
    def longestPalindrome(self, s: str) -> str:
        temp = -1
        stro=''
        for i in range(len(s)):
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1>temp):
                    temp=r-l+1
                    stro=s[l:r+1]
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1>temp):
                    temp=r-l+1
                    stro=s[l:r+1]
                l-=1
                r+=1
        return stro