class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frq = Counter(nums)
        max_frq = max(frq.values())
        ans = 0
        for i in frq.values():
            if i == max_frq:
                ans += i
        return ans