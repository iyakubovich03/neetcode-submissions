class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=[[] for i in range(len(nums)+1)]
        y={}
        for i in nums:
            y[i]=1+y.get(i,0)
        for j,p in y.items():
            l[p]+=[j]
        fin=[]
        z=0
        for i in range(len(l)-1,0,-1):
            if (len(l[i])!=0):
                for j in l[i]:
                    if(z==k):
                        return fin
                    z+=1
                    fin.append(j)
        return fin


    


        
        