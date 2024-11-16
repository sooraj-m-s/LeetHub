class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t = list(t)
        t.sort()
        s = list(s)
        s.sort()
        return s == t