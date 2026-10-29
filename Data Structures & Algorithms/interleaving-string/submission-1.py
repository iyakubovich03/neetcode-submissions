class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # valid interleaving is s1+t1+s2+.... (at most one difference is substring)
        # brute force: every possible parition of s1 and s2 and try to match to s3 recrusively tracking the current index at which we stopped the substring 
        # reach the end of s3 and the pointers of s2 and s1 are also at the end of the string then we can return True
        #if any of the poitners hit the end of teh string we can return false 
        #alterante between chossing substrings of s1 then to s2, or start from s2 then go to s1
        
        # dfs, where we hold the current pointer to each s1,s2 and s3, and we basiclly match that string if its not valid we cna break off 
        # 
        if len(s1)+len(s2)!=len(s3):
            return False

        memo={}
        def dfs(pointer_s1,pointer_s2):
            
            if  pointer_s1==len(s1) and pointer_s2==len(s2):
                return True 

            if (pointer_s1,pointer_s2) in memo:
                return memo[(pointer_s1,pointer_s2)]
        
            possible=False

            #left+right
            if pointer_s1<len(s1) and s3[pointer_s1+pointer_s2]==s1[pointer_s1]:
                possible=possible or dfs(pointer_s1+1,pointer_s2)
            
            if pointer_s2<len(s2) and s3[pointer_s1+pointer_s2]==s2[pointer_s2]:
                possible=possible or dfs(pointer_s1,pointer_s2+1)

            memo[(pointer_s1,pointer_s2)]=possible
            return memo[(pointer_s1,pointer_s2)]

        return dfs(0,0)


        # time len(s1)*len(s2)*len(pointer_s3) O(N^3) poloynimal runtime space is also O(N^3)


        # we are memorizing whether at (index1, index2) its possible to reach the end (bottom to up) or from the top to possibel to reach that position
