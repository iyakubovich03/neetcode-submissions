class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        starting_value=0
        for number in nums:
            starting_value^=number
        return starting_value
        