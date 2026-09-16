class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        temp=0
        right=len(s)
        top=[]
        while left<right:
            y=0
            top=[]
            for j in range(left,right,1):
                if s[j] in top:
                    left+=1
                    break
                y+=1
                top+=[s[j]]
                if (j == right-1) :
                    return max(temp,y)
            temp=max(temp,y)
        return temp

        