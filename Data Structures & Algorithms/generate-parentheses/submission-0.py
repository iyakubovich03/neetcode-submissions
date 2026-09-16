class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        
        def creater(op,cl):
            if op==cl==n:
                res.append("".join(stack))
                return
            if (op<n):
                stack.append("(")
                creater(op+1,cl)
                stack.pop()
            if (cl<op):
                stack.append(")")
                creater(op,cl+1)
                stack.pop()
        
        creater(0,0)
        return res