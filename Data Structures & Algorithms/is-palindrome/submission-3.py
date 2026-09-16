class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=''
        for i in s.lower():
            if i.isalpha() or i.isnumeric():
                l+=i
        return l == l[::-1]


        