class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap={"2":['a','b','c'], "3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"], "6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}

        result=[]
        current=[]
        def recursive(index):
            if index==len(digits):
                result.append("".join(current))#O(N)
                return
            
            currentCharacter=digits[index]
            for char in digitMap[currentCharacter]:
                current.append(char)
                recursive(index+1)
                current.pop()
                
        if not digits:
            return []

        recursive(0)
        return result
        
        