class Solution:
    def isValid(self, s: str) -> bool:
        #once we hit a closing value we check the stack if its the same we pop
        openingValue={"}":"{",")":"(","]":"["}
        previousValue=[]
        for character in s:
            if character in openingValue:
                if previousValue and previousValue[-1]==openingValue[character]:
                    previousValue.pop()
                else:
                    return False #meaning stack was empty or didnt euqal the same
            else:
                previousValue.append(character)

        return not previousValue


        