class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num = nums[i]
            k = target - num
            if k in nums and i != nums.index(k):
                return sorted([i, nums.index(k)])