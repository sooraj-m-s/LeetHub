class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        i, j = 0, 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                ans += word1[i]
                i += 1
            if j < len(word2):
                ans += word2[j]
                j += 1
        return ans