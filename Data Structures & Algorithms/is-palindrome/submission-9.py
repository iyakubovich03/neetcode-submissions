class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        s=s.lower()
        while (l<=r):
            if (not s[r].isalpha() and not s[r].isnumeric()):
                r-=1
                continue# moves
            if (not s[l].isalpha() and not s[l].isnumeric()):
                l+=1
                continue# moves 
            if (s[l]!=s[r]):
                return False
            l+=1
            r-=1

        return True



        