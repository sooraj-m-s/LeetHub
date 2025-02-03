class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = []
        cnt = 0
        for i in nums:
            if i == 1:
                cnt += 1
            if i == 0:
                ans += [cnt]
                cnt = 0
        ans += [cnt]
        return max(ans)