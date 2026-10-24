class Solution:
    def checkValidString(self, s: str) -> bool:
        #we can track every different possibility essentially 
        #consdiering that * can close an open, or add another open, or do nothing 
        min_open=0
        max_open=0
        for char in s:
            if char==")":
                #closed so this shirnk open for both regardless
                min_open-=1
                max_open-=1
            elif char=="(":
                min_open+=1
                max_open+=1
            else:
                #this is asymbol could either decrease open or increase open
                min_open-=1
                max_open+=1
            
            min_open=max(0,min_open)# no need to consider negative case
            if max_open<0:
                #means even after trying to use as many open parenthe not enoguh for clsoed
                return False
        return min_open==0 #all considerations possible if viable 
        # T: O(N)



        """
        #this apporach tracks the indexes of open parenthese, and weird symbol, and does stack operations, and tries to match the open with symbols if doesnt work then invlaid T: O(N) S: O(N)
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
        """
