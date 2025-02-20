class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        big = max(candies)
        ans = []
        for i in candies:
            ans.append(i + extraCandies >= big)
        return ans