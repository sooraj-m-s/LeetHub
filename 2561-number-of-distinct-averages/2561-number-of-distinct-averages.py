class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        average, ans = [], 0
        while len(nums) > 1:
            temp = ((nums.pop(0)+nums.pop())/2)
            if temp not in average:
                average.append(temp)
                ans += 1
        return ans