class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        top={"}":"{", "]":"[", ")": "("}


        for i in s:
            if i in top :
                if len(l)!=0 and l[-1]==top[i]:
                    l.pop()
                else:
                    return False
            else:
                l.append(i)
        
        return not l
