class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l=0
        r=len(s)-1
        while (l<r):
            while  l<r and not (s[l].isalpha()) and not(s[l].isnumeric()):
                l+=1
            while l<r and not (s[r].isalpha()) and not(s[r].isnumeric()):
                r-=1
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True



        