class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l=set()#will track location 
        #add as you go but recurse backwards if False and remove 
        if (word is None):
            return False
        def pot(tup,ind): #needs to make sure it deoesnt repeat the same positions 
            nonlocal board
            row,col=tup
            if (ind==len(word)):
                return True
            if (row>=len(board) or row<0 or col<0 or col>=len(board[0]) or (row,col) in l or board[row][col]!=word[ind]):
                return False#checking in bounds if not just return 
            #add position here 

    
            l.add((row,col))# have to always add so you dont repeat
            found=pot((row+1,col),ind+1) or pot((row-1,col),ind+1) or pot((row,col-1),ind+1) or pot((row,col+1),ind+1) # all possible expands forwad so once hits true will always be true 

            #remove it till the end 
            l.remove((row,col)) # how does this work once reaches base case 
            
            return found

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]==word[0]:
                    if (pot((row,col),0)):
                        return True
        return False
        #this calls the function based on if its there 

                #recursive call in 4 directions
                #always move in 4 direion  
            
            #recursive call in 4 directions if value equasl