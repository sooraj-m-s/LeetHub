class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i]-1) * (nums[j]-1) > ans:
                    ans = (nums[i]-1) * (nums[j]-1)
        return ans