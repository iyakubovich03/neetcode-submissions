class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        top = {}
        for l in nums:
            try: 
                top[l]+=1
            except(KeyError):
                top[l]=1
            
        for po in top:
            if top[po]>1:
                return True
            
        return False


         