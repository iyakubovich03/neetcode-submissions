class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        h=[]
        nums=sorted(nums)
        
        
        def pot(num,ind):
            nonlocal h
            nonlocal nums
           
           
            if ind>=len(nums):
                h.append(num) #for leafs
                return  #break condiion 
            val=nums[ind]
            if (nums[ind-1]==nums[ind] and nums[ind] in num):
                pot(num+[val],ind+1)
                return
            pot(num+[val],ind+1)# reutrn case of adding
            pot(num,ind+1)#return case of adding
                
        pot([],0)
        return h

        #how to delete w duplucaes
                



        