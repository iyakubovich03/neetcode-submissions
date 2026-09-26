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
            for ind in range(index,len(s)): #O(N)
                value=s[ind]
                check.append(value)
                if matrix[index][ind]: #O(N)-> O(N^2)
                    current.append("".join(check))#O(N)
                    recurse(ind+1)
                    current.pop()
            return 

        matrix=self.preWork(s)
        recurse(0)
        return result

    def preWork(self,s):
        matrix=[([False] * len(s)) for _ in range(len(s))]
        print(matrix)
        for row in range(len(s)): #base
            for col in range(row+1):
                matrix[row][col]=True
        
        #iterate from bottom up starting from range cell continue forward col 
        for row in range(len(s)-1,-1,-1):
            for col in range(row+1,len(s)):
                #basiclly check if euqal 
                matrix[row][col]=(s[row]==s[col] and matrix[row+1][col-1])
        print(matrix)
        return matrix

    

        #then we will itearte downards 



    """
    def isAnagram(self,word): # the check is the thing that is makign ths non optimal 
        l,r=0,len(word)-1
        while l<r: 
            if word[l]!=word[r]:
                return False
            l+=1
            r-=1
        return True

    """

        #not optimla solution 