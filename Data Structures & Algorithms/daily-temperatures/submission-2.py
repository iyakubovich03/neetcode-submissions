class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        p=[]
        l=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while p and t>p[-1][0]:
                stackind,stackval=p.pop()
                l[stackval]=i-stackval
            p.append([t,i])
        return l


        
        

        