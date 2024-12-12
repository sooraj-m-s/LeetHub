class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        temp = [str(i) for i in nums]
        ans = 0
        for i in temp:
            if len(i) % 2 == 0:
                ans += 1
        return ans