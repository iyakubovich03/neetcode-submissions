class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #that will try to match each character of one of hte strings to the toehr string and theirs two bases really either we reach the end of one or the end of another 
        


        #for each (m,n) state we want the maximum value subseqeunce at that point and if it matches we incrment it
        #how can we turn this into dp 

         
        dp=[[0]*len(text1) for _ in range(len(text2))]

        for row in range(len(dp)):
            for col in range(len(dp[0])):
                
                value_above=dp[row-1][col] if row>0 else 0
                value_left=dp[row][col-1] if col>0 else 0
                value_left_left=dp[row-1][col-1] if col>0 and row>0 else 0
                matching=1 if text1[col]==text2[row] else 0
                dp[row][col]=max(value_left,value_above,value_left_left +matching)

        return dp[-1][-1]
        





        """
        def dfs(current_text1_index,current_text_2_index):

            if current_text_2_index==len(text2):
                return 0 

            if current_text1_index==len(text1):
                return 0 

            if (current_text1_index,current_text_2_index) in memo:
                return  memo[(current_text1_index,current_text_2_index)]

            max_value=-float('inf')
            for index in range(current_text1_index,len(text1)): #O(N)
                current_char=text1[index]

                #check for each character matching 
                for index2 in range(current_text_2_index,len(text2)): #O(M)
                    current_matching=text2[index2]

                    if current_matching==current_char:
                        #then we recurse
                        max_value=max(max_value,dfs(index+1,index2+1)) #
            
            #at that index we idenity the longest subseuquence 
            memo[(current_text1_index,current_text_2_index)]=max_value+1
            return  memo[(current_text1_index,current_text_2_index)]


        # THere are M*N posisble states for the dfs and each state does M*N work , space: O(M*N)
        value=dfs(0,0)
        return value if value!=-float('inf') else 0
        

                #we try matching 
        """
            



        """
        dp=[[0]*len(text1) for _ in range(len(text2))]

        for row in range(len(dp)):
            for col in range(len(dp[0])):
                
                value_above=dp[row-1][col] if row>0 else 0
                value_left=dp[row][col-1] if col>0 else 0
                matching=1 if text1[col]==text2[row] else 0
                dp[row][col]=max(value_left,value_above+matching)

        return dp[-1][-1]
        """
