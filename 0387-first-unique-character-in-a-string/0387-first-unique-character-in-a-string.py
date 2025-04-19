class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        count = Counter(s)

        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1