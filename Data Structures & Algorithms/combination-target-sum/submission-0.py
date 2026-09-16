class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def pot(ret,ind,tot):
            nonlocal target
            nonlocal nums
            if tot>=target:#two base cases
                if tot==target and ret not in res:
                    res.append(ret)
                return
            if (ind>=len(nums)):#two base cases
                return
            val=nums[ind]
            pot(ret+[val],ind,tot+val)#this will allow you to add yourself as mnay times as you want 
            pot(ret+[val],ind+1,tot+val)# this will increment 
            pot(ret,ind+1,tot)
        pot([],0,0)
        return res
            

            