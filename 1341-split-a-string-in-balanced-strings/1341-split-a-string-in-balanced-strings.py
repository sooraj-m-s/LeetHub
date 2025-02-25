class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans, cnt = 0, 0
        for i in s:
            if i == 'R':
                cnt += 1
            elif i == 'L':
                cnt -= 1
            if cnt == 0:
                ans += 1
        return ans