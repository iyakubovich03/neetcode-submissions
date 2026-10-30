class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # when we can choose between operations (if we can replace over insert/delete we should less)
        # if we can already create word2 from word1, then all we need to do is delete characters (just take the difference in length)
        # what if we need to add chracters or replace characters


        memo={}

        def dfs(pointer_1,pointer_2):

            if pointer_2==len(word2):
                return len(word1)-pointer_1 #handles the case where we added to many charcters and need to delete them 

            if pointer_1==len(word1):
                return len(word2)-pointer_2

            if (pointer_1,pointer_2) in memo:
                return memo[(pointer_1,pointer_2)]

            min_operations=float('inf')

            deleting=1+dfs(pointer_1+1,pointer_2)
            #(f"min operations if we started at deleting {deleting}")
            replacing=1+dfs(pointer_1+1,pointer_2+1)
            #print(f"min operations if we started by replacing {replacing}")
            adding=1+dfs(pointer_1,pointer_2+1)
            #print(f"min operations if we started by adding {adding}")

            equality=dfs(pointer_1+1,pointer_2+1) if word1[pointer_1]==word2[pointer_2] else float('inf')
            #print(f"if current poitners are equal just skippping both {equality}")

            min_operations=min(deleting,replacing,adding,equality)
            #print(f" min operatoins required {min_operations} at pointer_1: {pointer_1} and at pointer_2 {pointer_2}")

            
            memo[(pointer_1,pointer_2)]=min_operations

            return memo[(pointer_1,pointer_2)]

    
        return dfs(0,0)