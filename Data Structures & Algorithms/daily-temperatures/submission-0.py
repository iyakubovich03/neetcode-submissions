class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        p={}
        l=[]
        for i in range(len(temperatures)):
            for j in range(i,len(temperatures),1):
                if temperatures[i]<temperatures[j]:
                    l.append(j-i)
                    break
                if (j==(len(temperatures)-1) and not(temperatures[i]<temperatures[j])):
                    l.append(0)
        return l
            

        
        

        