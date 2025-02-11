class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) < 2:
            return 1
        ans, temp = 0, 1
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                temp = 1
            elif s[i] == s[i+1]:
                temp += 1
            if temp > ans:
                ans = temp
        return ans