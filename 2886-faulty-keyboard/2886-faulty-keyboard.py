class Solution:
    def finalString(self, s: str) -> str:
        ans = []
        for i, j in enumerate(s):
            if j == 'i':
                ans = ans[::-1]
            else:
                ans.append(j)
        return ''.join(ans)