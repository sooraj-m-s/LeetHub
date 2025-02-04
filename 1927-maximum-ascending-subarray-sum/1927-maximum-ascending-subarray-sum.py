class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans, store = [], [nums[0]]
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                store.append(nums[i])
            else:
                ans.append(sum(store))
                store = [nums[i]]
        ans.append(sum(store))
        return max(ans)