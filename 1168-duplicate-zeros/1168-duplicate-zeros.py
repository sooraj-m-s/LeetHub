class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        trigger = 0
        for i in range(len(arr)-1):
            if arr[i] == 0 and trigger == 0:
                arr.insert(i,0)
                arr.pop()
                trigger = 1
                continue
            trigger = 0