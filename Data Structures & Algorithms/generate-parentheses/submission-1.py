class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result=[]
        current=[]

        def backtrack(openP,closeP): #numebr of ocmbioantions *N

            if len(current)==n*2:
                result.append("".join(current)) #O(N)
                return
            
            if openP<n:
                current.append("(")
                backtrack(openP+1,closeP)
                current.pop()
            
            if closeP<openP:
                current.append(")")
                backtrack(openP,closeP+1)
                current.pop()
        
        backtrack(0,0)
        return result