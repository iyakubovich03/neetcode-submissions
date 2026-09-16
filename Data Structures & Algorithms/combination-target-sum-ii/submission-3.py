class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def pot(pon,ind,sums):
            nonlocal target
            nonlocal candidates
            nonlocal res
            #you will add all possible values 
            #just get all possible values and when reaches ind check 
            if ind>=len(candidates):
                if sums == target:
                    res.append(pon)
                return
            val=candidates[ind]
            if (ind>0 and candidates[ind]==candidates[ind-1] and val in pon):
                pot(pon+[val],ind+1,sums+val)
                return
            pot(pon+[val],ind+1,sums+val)
            pot(pon,ind+1,sums)
        pot([],0,0)
        return res