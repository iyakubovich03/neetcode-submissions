class Solution:
    def checkValidString(self, s: str) -> bool:
        number_of_swaps=[]
        number_of_open_parentheses=[]
        
        for index,char in enumerate(s):
            if char=="(":
                number_of_open_parentheses.append(index)
            elif char==")":
                if number_of_open_parentheses:
                    number_of_open_parentheses.pop()
                else:
                    if number_of_swaps:
                        number_of_swaps.pop()
                    else:
                        return False
            else:
                number_of_swaps.append(index)

        #now we try to match each open parentehse with a valid option we iterate from the back of number of open parentehse 
        #if the last value of * is less than then its impossible 
        while number_of_open_parentheses and number_of_swaps and number_of_open_parentheses[-1]<number_of_swaps[-1]:
            number_of_open_parentheses.pop()
            number_of_swaps.pop()
        
           
        return len(number_of_open_parentheses)==0 #

        #the probelm here. FOr example "*(" simply uisng teh frequnecy of the number of swaps wont work here, you need to match each open parentehese with a valid symbol after it occurs
        #so we need to store indicies for btoh 