class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        large = max(nums)
        return nums.index(large)