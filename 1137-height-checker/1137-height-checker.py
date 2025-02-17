class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        ans = 0
        for i, j in enumerate(sorted_heights):
            if j != heights[i]:
                ans += 1
        return ans