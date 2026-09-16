class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=str(len(i))+"#"+i
        print(s)
        return s
    def decode(self, s: str) -> List[str]:
        res=[]
        ind = 0
        while (ind<len(s)):# dont go go over
            j=ind
            print(j)
            while (s[j]!="#"):#goes till finds #
                j+=1
            #number always before 
            
            leni=s[ind:j] #number here
            res.append(s[j+1 : j+1+(int(leni))])# starting 
            ind=j+1+int(leni)
        print(res)
        return res

