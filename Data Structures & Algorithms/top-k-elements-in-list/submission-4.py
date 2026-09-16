class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l={}
        for i in nums:
            if i in l:
                l[i]+=1
            else: 
                l[i]=1
        x = -1
        y=-1
        z=[]
        for i in range(k):
            x=-1
            y=-1
            for j in l :
                if (l[j]>x) & (j not in z):
                    x=l[j]
                    y=j
            z+=[y]
        return z
        
        