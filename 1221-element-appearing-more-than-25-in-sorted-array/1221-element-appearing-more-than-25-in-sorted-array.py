class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return arr[0]
        temp = len(arr) // 4
        for i in range(len(arr)):
            if arr[i] == arr[i + temp]:
                return arr[i]