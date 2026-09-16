class Solution:
    def hammingWeight(self, n: int) -> int:
        tot=0
        while n:
            tot+=n%2
            n=n>>1
        return tot

        