class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[0]*(n+1)
        for i in range(n+1):
            l[i]=self.checking(i)
        return l

    def checking(self,j: int)->int:
        tot=0
        while j:
            tot+=j%2
            j=j>>1
        return tot


        