class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        po = {")":"(", "}": "{", "]" : "["}
        for i in s:
            if i in po:
                if stack and stack[-1] == po[i]:
                    stack.pop()
                else: return False
            else:
                stack.append(i)
        return True if not stack else False
        
            