class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)

        dp[len(s)]=True

        for index in range(len(s)-1,-1,-1):
            for word in wordDict:
                end=index+len(word)

                if word==s[index:end] and dp[end]:
                    dp[index]=True
                    break

        return dp[0]
                #index 2 -2 (0,1,2)
        """
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
        """
        

                #otherwise valid 
