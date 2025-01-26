class Solution:
    def minimumChairs(self, s: str) -> int:
        ans = [0]
        cnt = 0
        for i in s:
            if i == 'E':
                cnt += 1
            elif i == 'L':
                ans.append(cnt)
                cnt -= 1
        ans += [cnt]
        return max(ans)