class Solution:
    def reverse(self, x: int) -> int:
        temp = abs(x)
        temp = [i for i in str(temp)]
        temp.reverse()
        ans = int(''.join(temp))
        if ans < -(2**31) or ans > (2**31-1):
            return 0
        if x < 0:
            return -ans
        return ans