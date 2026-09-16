class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        wo={}
        l=0
        val=0
        typ=0
        for r in range(len(s)):
            wo[s[r]]=wo.get(s[r],0)+1# adds val
            val=max(wo.values())
            while (r-l+1-val>k):
                wo[s[l]]=wo.get(s[l],0)-1
                l+=1
                val=max(wo.values())
            typ=max(typ,r-l+1)
        return typ
