class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        if len(t)>len(s):
            return 0

        memo={}

        def dfs(s_pointer,t_pointer):

            if t_pointer==len(t):
                return 1 

            if s_pointer==len(s):
                return 0

            if (s_pointer,t_pointer) in memo:
                return memo[(s_pointer,t_pointer)]

            distinct_ways=0

            if s[s_pointer]==t[t_pointer]:
                distinct_ways+=dfs(s_pointer+1,t_pointer+1)

            distinct_ways+=dfs(s_pointer+1,t_pointer)

            memo[(s_pointer,t_pointer)]=distinct_ways

            return memo[(s_pointer,t_pointer)]

        return dfs(0,0)


        