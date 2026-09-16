class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for i in strs:
            result+=str(len(i))+"#"+i
        return result

    def decode(self, s: str) -> List[str]:
        x=[]
        p=0
        while(p<len(s)):
            j=p
            while(s[j]!="#"):
                j+=1
            o=int(s[p:j])
            p=j+1
            j=p+o
            x+=[s[p:j:1]]
            p=j
            
        
        return x



