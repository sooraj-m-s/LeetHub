class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if len(s) % k != 0:
            s += fill * (k - len(s) % k)
        ans = []
        for i in range(0, len(s), k):
            ans.append(s[i: i+k])
        return ans