class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #slice the string (check if valid substring: if not continue) then recruse forward till we reach index==len(s) then append to result 
        #complexity wise thats not great
        result=[]
        current=[] 
        def recurse(index):
            if index==len(s):
                result.append(current.copy())
                return

            #we iterate over it and check the 
            check=[]
            for ind in range(index,len(s)):
                value=s[ind]
                check.append(value)
                if self.isAnagram(check):
                    current.append("".join(check))
                    recurse(ind+1)
                    current.pop()
            return 
        recurse(0)
        return result



    def isAnagram(self,word):
        l,r=0,len(word)-1
        while l<r: 
            if word[l]!=word[r]:
                return False
            l+=1
            r-=1
        return True