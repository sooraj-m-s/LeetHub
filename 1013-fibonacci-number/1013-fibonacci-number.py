class Solution:
    def fib(self, n: int) -> int:
        prv = 1
        nxt = 0
        for _ in range(n):
            temp = prv + nxt
            prv = nxt
            nxt = temp
        return nxt