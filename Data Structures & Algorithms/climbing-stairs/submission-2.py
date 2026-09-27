class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        oneStepAway=2 # index-
        twoStepAway=1 #index -2  

        for index in range(2,n):
            #update one stepaway 
            temp=oneStepAway
            oneStepAway=oneStepAway+twoStepAway
            twoStepAway=temp

        return oneStepAway
        