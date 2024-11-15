class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        temp = sorted(nums)
        return (temp[-2] * temp[-1]) - (temp[0] * temp[1])