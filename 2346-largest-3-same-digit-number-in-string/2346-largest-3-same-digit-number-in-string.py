class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ''
        for i in range(len(num)-2):
            window = num[i:i+3]
            if window[0] == window[1] == window[2]:
                result = max(result, window)
        return result