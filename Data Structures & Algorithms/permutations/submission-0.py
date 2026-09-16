class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        val=self.permute(nums[1:])# pushes down one
        res=[]
        for i in val:
            for j in range(len(i)+1):#this will add to eveyr possoble postion
                i_cop=i.copy()
                i_cop.insert(j,nums[0])
                res.append(i_cop)
        return res