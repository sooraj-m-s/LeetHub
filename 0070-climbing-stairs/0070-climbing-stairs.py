class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            prv = 1
            crnt = 1
            for i in range(n-1):
                temp = prv + crnt
                prv = crnt
                crnt = temp
            return crnt
        return fib(n)