class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        count={}
        res=0
        fin=0
        for r in range(len(s)):
            z=0
            count[s[r]]=1+count.get(s[r],0) #adds to the count
            res=max(res,count[s[r]]) #gives u the max over time
            if (r-l+1-res)>k:
                count[s[l]]-=1
                l+=1
            fin=max(fin,r-l+1)
        return fin
