class Solution:
    def numDecodings(self, s: str) -> int:

        """
        characterMap={str(index+1) for index in range(26)} #this can j be a set
    
        #exponentail 
        seen={}
        def recurse(index):
            if index==len(s):
                return 1
            if index in seen:
                return seen[index]
            value=0
            for ind in range(index,len(s)):
                #once we hit an invalid subset there is not point of conituing 
                subset=s[index:ind+1]
                if subset in characterMap:
                    value+=recurse(ind+1)
                else:
                    break
                seen[index]=value
            return value

        return recurse(0)
 
        """
        characterMap={str(index+1) for index in range(26)}
        dp=[0]*(len(s)+1)
        dp[len(s)]=1
         
        for index in range(len(s)-1,-1,-1):
            for index2 in range(index,len(dp)):
                subset=s[index:index2]
                if subset in characterMap:
                    dp[index]+=dp[index2]
        return dp[0]

