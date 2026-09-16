class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def pot(num,ind):
            nonlocal nums
            
            nonlocal res
            if ind>=len(nums):
                res.append(num)
                return
            val=nums[ind]
        
            
            pot(num+[val],ind+1)
            pot(num,ind+1)
        pot([],0)
        return res


        