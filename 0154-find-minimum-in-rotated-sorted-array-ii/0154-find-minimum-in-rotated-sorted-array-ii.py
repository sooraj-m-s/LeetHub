class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in nums:
            if ans > i:
                ans = i
        return ans