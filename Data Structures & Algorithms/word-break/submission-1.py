class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo={}
        def recursive(index):
            if index==len(s): #O(B)
                return True
            if index in memo: 
                return memo[index]
            found=False
            for word in wordDict: #O(N)
                ind=index#we enter while loop
                while ind<len(s) and (ind-index)<len(word) and word[ind-index]==s[ind]: #O(A)
                    ind+=1
                #check if we reached end of word 
                if (ind-index)!=len(word):
                    continue
                found=found or recursive(ind)
                
            memo[index]=found
            return found
        
        return recursive(0)
        #recurisvely check each word and explore each path 
                #otherwise valid 
