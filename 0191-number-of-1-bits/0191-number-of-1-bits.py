class Solution:
    def hammingWeight(self, n: int) -> int:
        temp = bin(n)
        return sum([int(i) for i in temp if i.isdigit()])