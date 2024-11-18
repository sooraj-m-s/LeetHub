class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        for _ in nums:
            if original in nums:
                original = original * 2
            else:
                break
        return original