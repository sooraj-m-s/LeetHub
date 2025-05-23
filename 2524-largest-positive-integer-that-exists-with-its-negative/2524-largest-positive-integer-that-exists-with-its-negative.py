class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = []
        for i in nums:
            if i < 0 and abs(i) in nums:
                ans.append(abs(i))
        if ans:
            return max(ans)
        return -1