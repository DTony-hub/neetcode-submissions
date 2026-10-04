class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_2 = nums
        nums = nums + nums_2
        return nums