class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""

        tFrequency=defaultdict(int)
        sFrequency=defaultdict(int)

        for character in t:
            tFrequency[character]+=1


        uniqueKeys=len(tFrequency)

        shortestStart=-1
        shortestLength=float('inf')

        currentPoints=0
        l=0

        for index,character in enumerate(s):
            sFrequency[character]+=1
            if character in tFrequency and sFrequency[character]==tFrequency[character]:
               
                currentPoints+=1
      
            while currentPoints==uniqueKeys:

                #take min
                if index-l+1<shortestLength:
                    shortestLength=index-l+1
                    shortestStart=l

                sFrequency[s[l]]-=1
                if s[l] in tFrequency and sFrequency[s[l]]+1==tFrequency[s[l]]:
                    currentPoints-=1

                l+=1

        return s[shortestStart:shortestStart+shortestLength] if shortestStart!=-1 else ""
                
                
