class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in grid:
            i.sort(reverse=True)
        ans = 0
        for i in range(len(grid[0])):
            max_val = 0
            for j in grid:
                max_val = max(max_val, j[i])
            ans += max_val
        return ans