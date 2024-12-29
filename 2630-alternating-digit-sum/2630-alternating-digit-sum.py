class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        ans = []
        for i in range(len(n)):
            if i % 2 == 0:
                ans.append(int(n[i]))
            else:
                ans.append(-int(n[i]))
        return sum(ans)