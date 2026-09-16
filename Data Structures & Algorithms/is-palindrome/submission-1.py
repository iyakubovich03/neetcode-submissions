class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.upper()
        p=""
        for l in s:
            if l.isalpha() or l.isnumeric():
                p+=l
        return p == p[::-1]


        
        