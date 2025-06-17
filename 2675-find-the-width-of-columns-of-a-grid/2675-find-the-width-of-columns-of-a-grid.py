class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = [0] * len(grid[0])
        for i in grid:
            for j, val in enumerate(i):
                ans[j] = max(ans[j], len(str(val)))
        return ans