class Solution:
    def rob(self, nums: List[int]) -> int:
        #you want to maximize the sum but you must make sure that you there are no adjacent
        #values
        #idea we recruse to non adjacent neighbors and test it out
        #if i wasnt tracking 
        
        shop2=0
        shop1=0
        for i in nums:
            temp=max(shop1,shop2+i)
            shop2=shop1
            shop1=temp
        return shop1#?