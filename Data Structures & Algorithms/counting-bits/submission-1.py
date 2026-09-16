class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[0]*(n+1)
        t=1
        for i in range(1,n+1):
            if i==t*2:
                t=i
            l[i]=1+l[i-t]
        return l


        