class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = [-1]
        for i in arr:
            if i == arr.count(i):
                ans.append(i)
        return max(ans)