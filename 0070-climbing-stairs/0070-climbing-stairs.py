class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        prv, crnt = 1, 1
        for i in range(n-1):
            temp = prv + crnt
            prv = crnt
            crnt = temp
        return crnt