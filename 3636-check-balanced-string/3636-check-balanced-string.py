class Solution:
    def isBalanced(self, num: str) -> bool:
        even = 0
        odd = 0
        for i, j in enumerate(num):
            if i % 2 == 0:
                even += int(j)
            else:
                odd += int(j)
        return even == odd