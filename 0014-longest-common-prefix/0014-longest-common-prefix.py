class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short = min(strs, key=len)
        for i, j in enumerate(short):
            for k in strs:
                if j != k[i]:
                    return short[:i]
        return short