class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        current=[]
        result=[]
        check=[False for _ in range(len(nums))]

        def recurse(index):
            if len(current)==len(nums):
                result.append(current.copy())
                return

            for ind in range(len(nums)):
                valid_index=(index+ind)%len(nums)
                value=nums[valid_index]

                if check[valid_index]:
                    continue #skip already in

                current.append(value)
                check[valid_index]=True
                recurse(index+1)
                current.pop()
                check[valid_index]=False
        recurse(0)
        return result
            
            #now we loop for the range 
            
        