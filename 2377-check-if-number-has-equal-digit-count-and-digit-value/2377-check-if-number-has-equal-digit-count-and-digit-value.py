class Solution:
    def digitCount(self, num: str) -> bool:
        frequency = {}
        for i in num:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        for i, j in enumerate(num):
            expected_count = int(j)
            actual_count = frequency.get(str(i), 0)
            if expected_count != actual_count:
                return False
        return True