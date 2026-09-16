class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l={}
        t=[[] for i in range(len(nums)+1)]
        fin=[]
        for i in nums:
            l[i]=l.get(i,0)+1 #filled dict w freq
        for j in l:
            t[l[j]].append(j)
        #should have an array w freq
        temp=len(nums)-1
        while k>0:
            while (k>0 and len(t[temp])!=0):
                fin.append(t[temp].pop())
                k-=1
            temp-=1

        return  fin

#you want to access it 