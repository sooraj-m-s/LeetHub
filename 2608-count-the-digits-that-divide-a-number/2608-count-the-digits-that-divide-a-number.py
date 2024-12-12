class Solution:
    def countDigits(self, num: int) -> int:
        temp = [int(i) for i in str(num)]
        ans = 0
        for i in temp:
            if num % i == 0:
                ans += 1
        return ans