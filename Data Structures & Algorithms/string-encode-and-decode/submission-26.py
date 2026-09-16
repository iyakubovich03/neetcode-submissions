class Solution:

    def encode(self, strs: List[str]) -> str:
        #return a string numberofCharacters# (as the stoopper)
        resultingString=[]
        for st in strs:
            resultingString.append("".join([str(len(st)),"#",st]))
        return "".join(resultingString)
        


    def decode(self, s: str) -> List[str]:
        index=0
        result=[]
        while index<len(s):
            j=index 
            number=[]
            while s[j]!="#":
                number.append(s[j])
                j+=1
            #now we have the number
            number=int("".join(number))
            current=[]
            for ind in range(j+1,j+1+number):
                current.append(s[ind])
            result.append("".join(current))
            #then move up 
            index=j+1+number
        return result


