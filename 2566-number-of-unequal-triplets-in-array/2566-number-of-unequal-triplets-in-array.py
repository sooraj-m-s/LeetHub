class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] != nums[j] != nums[k] and nums[i] != nums[k]:
                        ans += 1
        return ans