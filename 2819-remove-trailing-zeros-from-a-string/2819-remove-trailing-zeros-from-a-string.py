class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num_list, ind = list(num), len(num)-1
        while True:
            if num[ind] == '0':
                num_list.pop()
                ind -= 1
            else:
                break
        return ''.join(num_list)