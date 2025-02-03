class Solution:
    def checkString(self, s: str) -> bool:
        if 'b' not in s:
            return True
        a, b = -1, 0
        for i in range(len(s)):
            if s[i] == 'a':
                a = i
            elif b == 0:
                b = i
        return a < b